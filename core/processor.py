import json
import timeit
from extras import tools as tl
from extras import googleCSE as gcse
from core import configfile
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO
                    # ,handlers=[
                    #     logging.FileHandler("{0}/{1}.log".format("/Users/wangcongcong/Desktop/rectrts/dataset/log/", configfile.SUBMIT_FILE_NAME)),
                    # ]
                    )

class Processor:
    def __init__(self, model_name=configfile.MODEL):
        self.profiles = Processor.load_profiles()
        logging.info("The selected mode: "+model_name)
        logging.info("The filtering result will be written to:"+configfile.SUBMIT_FILE_NAME)
        logging.info("Query Expansion is applied?:"+ str(configfile.EXPANSION))
        if model_name == "Jaccard":
            from models import jaccardModel
            self.model_name = model_name
            self.model = jaccardModel
        elif model_name == "cosinetfidf":
            from models import cosinetfidf as cti
            from core.local_listener import LocalListener
            ll = LocalListener()
            logging.info("Model cosinetfidf is computing IDF...")
            tweets_collection = ll.get_topn_status(10000)
            all_tweets_batch = list(tweets_collection)
            cti.computeIDFByDocs(all_tweets_batch)
            logging.info("Model cosinetfidf is done computing IDF")
            self.model_name = model_name
            self.model=cti

    @classmethod
    def load_profiles(cls):
        with open("../dataset/TRECdataset/TREC2017-RTS-topics-final-expansion.json") as f:
            loaded_profiles = json.load(f)
        return loaded_profiles

    def start(self, tweet):
        count=0
        for profile in self.profiles:
            # print("processing profile:",count)
            count+=1
            # profile_tokens = self.expand_query(profile)
            # if not applying query expansion, comment  the above line and comment out the line below
            if configfile.EXPANSION:
                profile_tokens=profile["expansion"]
            else:
                profile_tokens=self.preprocess(profile['title']+" "+profile['description'])
            tweet_tokens = self.preprocess(tweet[3])
            relscore=self.compute_relevance(tweet_tokens, profile_tokens)
            # print("The consine similarity between profile ", profile['topid'], "(", profile['title'], ") and ",
            #       tweet[3], "(", tweet[0], "): ")
            if relscore>0.3:
                # print(relscore)
                # self.compute_redundancy(" ", " ")
                # self.ranking(" ")
                from datetime import datetime
                # created = int(tweet[2])
                # datetime=datetime.utcfromtimestamp(ts).strftime('%m%d-%H:%M:%S')
                self.submit_result(profile['topid'], tweet[0], tweet[2], score=relscore)

    def expand_query(self, profile):
        profile_title = profile['title']
        query_title_expanded_by_google = gcse.expand_by_google_url(profile_title)
        profile_desc = profile['description']
        query_expaned_tokens = query_title_expanded_by_google + tl.textParse(profile_desc)
        return query_expaned_tokens

    @classmethod
    def expandQuery(cls, profile):
        profile_title = profile['title']
        query_title_expanded_by_google = gcse.expand_by_google_url(profile_title)
        profile_desc = profile['description']
        query_expaned_tokens = query_title_expanded_by_google + tl.textParse(profile_desc)
        return query_expaned_tokens

    def preprocess(self, text):
        tokens = tl.textParse(text)
        return tokens

    def compute_relevance(self, tweet_info, profile_info):
        # print("compute_relevance")
        simscore=0
        if self.model_name=="Jaccard":
            simscore = self.model.calcualteSim(profile_info, tweet_info)
        elif self.model_name=="cosinetfidf":
            profilevec=self.model.getDFIDFVector(profile_info)
            tweetvec=self.model.getDFIDFVector(tweet_info)
            simscore=self.model.get_cosine(profilevec,tweetvec)
        return simscore

    def compute_redundancy(self, tweet1, tweet2):
        print("compute redundancy")
        pass

    def ranking(self, candidate_tweets):
        print("ranking")
        pass
#Scenario A format: RTS46	891133525792931840	0729-03:10:09	BJUT-BL1-04
    def submit_result(self, topicid,tweetid,time,runanme=configfile.SUBMIT_FILE_NAME,score=0):
        with open("../submission/"+runanme,"a") as f:
            submit_str=topicid+"\t"+tweetid+"\t"+time+"\t"+runanme+"\t"+str(score)+"\n"
            f.write(submit_str)

# def timetest():
#     profile_title = "HPV vaccine side effects"
#     from extras import googleCSE as gcse
#     query_title_expanded_by_google = gcse.expand_by_google(profile_title)
#     profile_desc = "Information concerning possible side effects of the HPV vaccine"
#     query_expaned_tokens = query_title_expanded_by_google + tl.textParse(profile_desc)
#     print(query_expaned_tokens)
# print(timeit.timeit("timetest()", number=1,setup="from __main__ import timetest"))

if __name__ == '__main__':
    pass
    # profiles=Processor.load_profiles()
    # import pprint
    #
    # count=1
    # for profile in profiles:
    #     print("Process expansion...:",count)
        # profile["expansion"]=Processor.expandQuery(profile)
        # count+=1
    # import json
    # with open('../dataset/TRECdataset/TREC2017-RTS-topics-final-expansion.json', 'w') as fout:
    #     json.dump(profiles, fout)

    # check = 0
    # if check == 0:
    #     p = Processor()
    #     p.start((2, 3, 4, "UCD"))
    # else:
    #     with open("../dataset/TRECdataset/TREC2017-RTS-topics-final.json") as f:
    #         from core.local_listener import LocalListener
    #         ll = LocalListener()
    #         profiles = json.load(f)
    #         from models import cosinetfidf as cti
    #         tweets_collection = ll.get_topn_status(1000)
    #         all_tweets_batch = list(tweets_collection)
    #         cti.computeIDFByDocs(all_tweets_batch)
    #         profile46vector = {}
    #         terminator = 0
    #         for profile in profiles:
    #             if terminator == 0:
    #                 profile_title = profile['title']
    #                 from extras import googleCSE as gcse
    #
    #                 query_title_expanded_by_google = gcse.expand_by_google(profile_title)
    #                 profile_desc = profile['description']
    #                 query_expaned_tokens = query_title_expanded_by_google + tl.textParse(profile_desc)
    #
    #                 profile46vector = cti.getDFIDFVector(query_expaned_tokens)
    #                 print("query_expaned_tokens:", query_expaned_tokens)
    #                 tweetsSteamBatch = ll.get_status_by_topic(profile['topid'])
    #                 # tweetsSteamBatch=tweets_collection
    #                 for tweetstream in tweetsSteamBatch:
    #                     tweettokens = tl.textParse(tweetstream[1])
    #                     tweetvector = cti.getDFIDFVector(tweettokens)
    #                     simscore = cti.get_cosine(profile46vector, tweetvector)
    #                     print("The consine similarity between profile ", profile['topid'], "(", profile_title, ") and ",
    #                           tweetstream[0], "(", tweetstream[1], "): ")
    #                     print("based on TF-IDF: ", simscore)
    #                     print("labelled: ", tweetstream[3])
    #                 # print(query_expaned_tokens)
    #             terminator += 1

        # print()
        # print(len(ll.get_status_by_topic('RTS46')))
        # tl.test()
        # profiles[0]['description']
        # profiles[0]['title'] + " " + profiles[0]['description']
        # profiles[0]['narrative']
        # print(p[r])
        # pro=Processor()
        # pro.expand_query(query=)
        # pro.preprocess()
