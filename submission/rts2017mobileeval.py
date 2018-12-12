#!/usr/bin/python

# This is the evaluation script for the TREC 2017 RTS evaluation
# (scenario A) with mobile assessor judgments, v1.00. Based on
# TREC 2016 RTS evaluatio script.
#
# Release History:
#
# - v1.00 (Sept 2017): Original release

__author__ = 'Luchen Tan'
import numpy
import argparse
import sys
from datetime import datetime

# evaluation_starts = 1501286400
# evaluation_ends = 1501977599
# seconds_perday = 86400
def evaluate(run_path, printswitch=False):
    K = 10
    days = []
    for i in range(29, 32):
        days.append("201707%02d" % i)
    for i in range(1, 6):
        days.append("201708%02d" % i)
    unixTimestamp = datetime.utcfromtimestamp(0)
    file_qrels_path = "submission/support/rts2017-mobile-qrels.txt"
    # run_path="/Users/wangcongcong/Desktop/rectrts/dataset/TRECdataset/submissions/scenarioA/advanse_lirmm-Run1-A"
    file_tweet2day = "submission/support/rts2017-mobile-tweets2dayepoch.txt"
    # the result will be the same if running on the following file
    # file_tweet2day = "../log-tweetIds-in-db-2017-and-epoch.txt"
    # print(unixTimestamp)
    # print(args)
    # print(file_qrels_path)
    # print(run_path)
    # print(file_tweet2day)
    # qrels_dt = {topic: {tweetid: [#rel, #non_rel, #redundant]}}
    qrels_dt = {}
    for i, line in enumerate(open(file_qrels_path)):
        line = line.strip().split()
        topic = line[0]
        tweetid = line[1]
        judgement = int(line[2])
        if topic not in qrels_dt:
            qrels_dt[topic] = {tweetid: [0, 0, 0]}
        if tweetid not in qrels_dt[topic]:
            qrels_dt[topic][tweetid] = [0, 0, 0]
        if judgement == 1:
            qrels_dt[topic][tweetid][0] += 1
        elif judgement == 2:
            qrels_dt[topic][tweetid][2] += 1
        elif judgement == 0:
            qrels_dt[topic][tweetid][1] += 1

    # created timestamp for each tweetid in the qrel
    # tweet2epoch_dt: {tweetid: epoch time}
    tweet2epoch_dt = {}
    for line in open(file_tweet2day).readlines():
        line = line.strip().split()
        tweet2epoch_dt[line[0]] = int(line[2])
    runname = ""
    run_dt = {topic: 0 for topic in qrels_dt}
    rel_dt = {topic: 0 for topic in qrels_dt}
    non_rel_dt = {topic: 0 for topic in qrels_dt}
    redun_dt = {topic: 0 for topic in qrels_dt}
    unjudge_dt = {topic: 0 for topic in qrels_dt}
    delay_list = {topic: [] for topic in qrels_dt}
    all_delay = []
    run_lines = open(run_path).readlines()
    if len(run_lines) == 0:
        # print("This is an empty run.")
        return "\t".join([run_path.split("/")[1], "All", "0","0","0","0","0","0","0","0","0","0"])
        # sys.exit()

    for line in run_lines:
        line = line.strip().split()
        runname = line[3]
        topic = line[0]
        if topic in qrels_dt:
            run_dt[topic] += 1
            tweetid = line[1]
            pushed_at = datetime.strptime("17" + line[2], "%y%m%d-%H:%M:%S")
            epoch = int((pushed_at - unixTimestamp).total_seconds())
            if tweetid in tweet2epoch_dt:
                created_at = tweet2epoch_dt[tweetid]
                # -------ADD
                # epoch=epoch+3600
                # --------ADD
                if epoch >= created_at and tweetid in qrels_dt[topic]:
                    rel_dt[topic] += qrels_dt[topic][tweetid][0]
                    non_rel_dt[topic] += qrels_dt[topic][tweetid][1]
                    redun_dt[topic] += qrels_dt[topic][tweetid][2]
                    # any judged tweet is counted in delay
                    # not only relevant tweets
                    delay = epoch - created_at
                    delay_list[topic].append(delay)
                    all_delay.append(delay)
                else:
                    unjudge_dt[topic] += 1
            else:
                unjudge_dt[topic] += 1
    # import pprint
    # pprint.pprint(tweet2epoch_dt)
    # pprint.pprint(run_dt)
    # pprint.pprint(unjudge_dt)

    # in the final results, #rel + #non-rel + #redundant could be larger than total length
    # since we are counting each assessment from the crowd
    # print("\t".join(["Threshold","run", "topic", "relevant", "redundant", "not_relevant",
    #                  "online_utility(strict)", "online_utility(lenient)",
    #                  "unjudged", "total_length", "mean_latency", "median_latency"]))

    str_my = ",".join(["run", "topic", "relevant", "redundant", "not_relevant",
                       "online_utility(strict)", "online_utility(lenient)",
                       "unjudged", "total_length", "mean_latency", "median_latency"])
    coverage = 0
    onlineU_strict = {topic: rel_dt[topic] - redun_dt[topic] - non_rel_dt[topic] for topic in rel_dt}
    onlineU_lenient = {topic: rel_dt[topic] + redun_dt[topic] - non_rel_dt[topic] for topic in rel_dt}

    for topic in sorted(qrels_dt.keys()):
        if run_dt[topic] > 0:
            coverage += 1
        if printswitch:
            print("\t".join([runname, topic, str(rel_dt[topic]), str(redun_dt[topic]), str(non_rel_dt[topic]),
                             str(onlineU_strict[topic]),
                             str(onlineU_lenient[topic]),
                             str(unjudge_dt[topic]), str(run_dt[topic]),
                             str(round(numpy.mean(delay_list[topic]) if delay_list[topic] != [] else 0, 1)),
                             str(round(numpy.median(delay_list[topic]) if delay_list[topic] != [] else 0, 1))]))
    return "\t".join([runname, "All", str(sum(list(rel_dt.values()))),
                      str(sum(list(redun_dt.values()))), str(sum(list(non_rel_dt.values()))),
                      str(sum(list(onlineU_strict.values()))), str(sum(list(onlineU_lenient.values()))),
                      str(sum(list(unjudge_dt.values()))), str(sum(list(run_dt.values()))),
                      str(round(numpy.mean(all_delay) if all_delay != [] else 0, 1)),
                      str(round(numpy.median(all_delay) if all_delay != [] else 0, 1)), str(coverage / len(qrels_dt))])

