import json
import timeit
from extras import tools as tl


class Processor:

    def __init__(self):
        pass

    def expand_query(self, query):
        print("this is expand_query class")
        pass

    #
    def preprocess(self, tweet):
        print(tweet, " is preprocessing")
        pass

    def compute_relevance(self, tweet, profile):
        print("compute_relevance")
        pass

    def compute_redundancy(self, tweet1, tweet2):
        print("compute redundancy")
        pass

    def ranking(self, candidate_tweets):
        print("ranking")
        pass

    def submit_results(self, results):
        print("submit results")
        pass

# def timetest():
#     profile_title = "HPV vaccine side effects"
#     from extras import googleCSE as gcse
#     query_title_expanded_by_google = gcse.expand_by_google(profile_title)
#     profile_desc = "Information concerning possible side effects of the HPV vaccine"
#     query_expaned_tokens = query_title_expanded_by_google + tl.textParse(profile_desc)
#     print(query_expaned_tokens)
# print(timeit.timeit("timetest()", number=1,setup="from __main__ import timetest"))

if __name__ == '__main__':
    with open("../dataset/TRECdataset/TREC2017-RTS-topics-final.json") as f:
        from core.local_listener import LocalListener
        ll = LocalListener()
        profiles = json.load(f)
        from models import cosinetfidf as cti
        tweets_collection = ll.get_topn_status(1000)
        all_tweets_batch = list(tweets_collection)
        cti.computeIDFByDocs(all_tweets_batch)
        profile46vector={}
        terminator = 0
        for profile in profiles:
            if terminator == 5:
                profile_title = profile['title']
                from extras import googleCSE as gcse
                query_title_expanded_by_google = gcse.expand_by_google(profile_title)
                profile_desc = profile['description']
                query_expaned_tokens = query_title_expanded_by_google + tl.textParse(profile_desc)
                profile46vector=cti.getDFIDFVector(query_expaned_tokens)
                print("query_expaned_tokens:",query_expaned_tokens)
                tweetsSteamBatch = ll.get_status_by_topic(profile['topid'])
                # tweetsSteamBatch=tweets_collection
                for tweetstream in tweetsSteamBatch:
                    tweettokens = tl.textParse(tweetstream[1])
                    tweetvector = cti.getDFIDFVector(tweettokens)
                    simscore = cti.get_cosine(profile46vector, tweetvector)
                    print("The consine similarity between profile ",profile['topid'],"(",profile_title,") and ", tweetstream[0], "(", tweetstream[1],"): ")
                    print("based on TF-IDF: ", simscore)
                    print("labelled: ", tweetstream[3])
                # print(query_expaned_tokens)
            terminator += 1
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