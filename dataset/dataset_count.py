
def rts_mobile_dataset_count():
    uni_topic_dict={}
    uni_tweet_dict = {}
    uni_topic_count=0
    uni_tweet_count=0
    with open("TRECdataset/rts2017-mobile-qrels.txt") as f:
        alllines = f.read().split("\n")
        for eachline in alllines:
            linecolumns=eachline.split()
            # if linecolumns[0] not in uni_topic_dict:
            #     # uni_topic_count+=1
            #     uni_topic_dict[linecolumns[0]]=1
            if linecolumns[1] not in uni_tweet_dict:
                # uni_tweet_count+=1
                uni_tweet_dict[linecolumns[1]]=1
    with open("TRECdataset/rts2017-batch-qrels.txt") as f:
        alllines = f.read().split("\n")
        for eachline in alllines:
            linecolumns = eachline.split()
            if linecolumns[0] not in uni_topic_dict:
                uni_topic_count += 1
                uni_topic_dict[linecolumns[0]] = 1
            if linecolumns[2] not in uni_tweet_dict:
                uni_tweet_count += 1
                uni_tweet_dict[linecolumns[2]] = 1
    print("Unique topics: ",uni_topic_count)
    print("Unique tweets: ",uni_tweet_count)

def regenerate_file(sourcefile,destinationfile):
    with open(sourcefile,"r") as sf:
        alllines = sf.read().split("\n")
        for eachline in alllines:
            #$ get all tweep errors
            if "Rate limit" not in eachline:
                with open(destinationfile,"a") as df:
                    df.write(eachline+"\n")

def get_tweep_error_record(filename):
    repeat_check_dict={}
    with open(filename,"r") as sf:
        tweeperrorscount={}
        alllines = sf.read().split("\n")
        for eachline in alllines:
            errorstring=eachline.split("@")[1]
            tweetid=eachline.split("@")[0]
            if tweetid not in repeat_check_dict:
                repeat_check_dict[tweetid]=1
            else:
                if errorstring in tweeperrorscount:
                    tweeperrorscount[errorstring]+=1
                else:
                    tweeperrorscount[errorstring]=1
    return tweeperrorscount




def count_rate_limit_error(filename):
    alltweetsidwithratelimiterror={}
    with open(filename,"r") as sf:
        alllines = sf.read().split("\n")
        for eachline in alllines:
            #$ get all rate limit errors
            if "Rate limit exceeded" in eachline:
                # store all unique tweet ids with rate limit error
                tweetid=eachline.split("@")[0]
                if tweetid not in alltweetsidwithratelimiterror:
                    with open("tweets-with-rate-limit.txt","a") as f:
                        f.write(tweetid+"\n")
                    alltweetsidwithratelimiterror[tweetid]=1
    return alltweetsidwithratelimiterror
if __name__ == '__main__':
    # print(get_tweep_error_record("error_log_sql_excluded.txt"))
    rts_mobile_dataset_count()

    # regenerate_file("error_log_sql_excluded.txt","error_log_sql_excluded.txt")
    # alltweetsidwithratelimiterror= count_rate_limit_error("error_log_sql_excluded.txt")
    # print("the number of all unqiue tweets with rate limit: ",len(alltweetsidwithratelimiterror))