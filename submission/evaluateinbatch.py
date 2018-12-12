def eval2017Mobile(file2evaluate):
    from DB.submission import rts2017mobileeval as me
    print("\t".join(["run", "topic", "relevant", "redundant", "not_relevant",
                     "online_utility(strict)", "online_utility(lenient)",
                     "unjudged", "total_length", "mean_latency", "median_latency", "Coverage"]))
    print(me.evaluate("submission/"+file2evaluate, printswitch=True))


def eval2017BatchA(file2evaluate):
    from DB.submission import rts2017batchAeval as bae
    print("\t".join(["runtag", "topic",
                     "EGp", "EG1", "nCGp", "nCG1",
                     "GMP.33", "GMP.50", "GMP.66",
                     "mean_latency", "median_latency",
                     "total_length"]))
    print(bae.evaluate("submission/"+file2evaluate, printswitch=True))


def rts2017Mobileeval(files2evaluate):
    from DB.submission import rts2017mobileeval as me
    returnstr = "\t".join(["Threshold", "run", "topic", "relevant", "redundant", "not_relevant",
                           "online_utility(strict)", "online_utility(lenient)",
                           "unjudged", "total_length", "mean_latency", "median_latency", "Coverage"])+"\n"
    for k, v in files2evaluate.items():
        returnstr += str(v) + "\t" + me.evaluate(k, printswitch=False)+"\n"
    return returnstr


def rts2017BatchAeval(files2evaluate):
    from DB.submission import rts2017batchAeval as bae
    returnstr = "\t".join(["Threshold", "runtag", "topic",
                           "EGp", "EG1", "nCGp", "nCG1",
                           "GMP.33", "GMP.50", "GMP.66",
                           "mean_latency", "median_latency",
                           "total_length"])+"\n"
    for k, v in files2evaluate.items():
        returnstr += str(v) + "\t" + bae.evaluate(k, printswitch=False)+"\n"
    return returnstr


def eval2017MobileBatch(filestoeval):
    from DB.submission import rts2017mobileeval as me
    returnstr = "\t".join(["run", "topic", "relevant", "redundant", "not_relevant",
                           "online_utility(strict)", "online_utility(lenient)",
                           "unjudged", "total_length", "mean_latency", "median_latency", "Coverage"]) + "\n"
    for filepath in filestoeval:
        returnstr +=  me.evaluate(filepath, printswitch=False) + "\n"
    return returnstr


def eval2017BatchABatch(filestoeval):
    from DB.submission import rts2017batchAeval as bae
    returnstr = "\t".join([ "runtag", "topic",
                           "EGp", "EG1", "nCGp", "nCG1",
                           "GMP.33", "GMP.50", "GMP.66",
                           "mean_latency", "median_latency",
                           "total_length"]) + "\n"
    for filepath in filestoeval:
        returnstr += bae.evaluate(filepath, printswitch=False) + "\n"
    return returnstr


def eval2017BBatch(filestoeval):
    from DB.submission import rts2017batchBeval as bbe
    returnstr=""
    returnstr += "{0}\t{1:5s}\t{2:6s}\t{3:6s}".format("runtag", "topic", "nDCGp", "nDCG1") + "\n"
    for filepath in filestoeval:
        returnstr += bbe.evaluate(filepath, printswitch=False) + "\n"
    return returnstr