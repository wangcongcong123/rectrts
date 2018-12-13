import datetime
import time
import timeit

import tweepy
import core.dbtools as dbtools
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO
                    # ,handlers=[
                    #     # logging.FileHandler("{0}/{1}.log".format("/Users/wangcongcong/Desktop", "gensim")),
                    #     logging.StreamHandler()
                    # ]
                    )

class OnlineListener(tweepy.StreamListener):

    def setParaUp(self, executor):
        self.executor = executor
        self.statusbatch = []
        self.batchsize = 100
        self.count = 0
        self.start = timeit.default_timer()
        self.stop = timeit.default_timer()

    def on_status(self, status):
        # if return
        if status.retweeted:
            return
        tweet=status._json
        if tweet["lang"] !="en":
            return

        # if self.batchsize == 0:
        #     print("Time consumed: ", str(self.stop - self.start))
        #     self.start = timeit.default_timer()
        #     dbtools.status2dbbatch(self.statusbatch)
        #     self.batchsize = 100
        #     self.statusbatch = []
        # self.stop = timeit.default_timer()
        # self.statusbatch.append(status)
        # self.batchsize -= 1
        # print("Get Tweet", self.count)
        # self.executor.excute(status)
        self.count += 1
        rebuild_tweet=self.tweetRebuilt(status)
        self.executor.excute(rebuild_tweet)
        logging.info("Processing Tweet " + str(self.count)+" : ")

    def on_error(self, status_code):
        if status_code == 420:
            return False

    def tweetRebuilt(self,tweet):
        id = tweet.id_str
        status_json = tweet._json
        if "retweeted_status" in status_json:
            status_text = status_json['retweeted_status']['text']
        else:
            status_text = status_json['text']

        created_time = tweet.created_at
        created_time=str(created_time)
        # print(created_time)
        # 2017-08-04 03:02:39
        reformattime = created_time.split()[0].split("-")[1] + created_time.split()[0].split("-")[2] + "-" + \
                       created_time.split()[1]
        rebuild_tweet = (id, created_time.split()[0].replace("-", ""), reformattime, status_text)

        return rebuild_tweet
