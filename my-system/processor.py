import json
from extras import tools as tl

class Processor:
    def __init__(self):
        pass

    def expand_query(self,query):
        print("this is expand_query class")
        pass

#
    def preprocess(self,tweet):
        print(tweet," is preprocessing")
        pass

    def compute_relevance(self,tweet, profile):
        print("compute_relevance")
        pass

    def compute_redundancy(self, tweet1, tweet2):
        print("compute redundancy")
        pass

    def ranking(self,candidate_tweets):
        print("ranking")
        pass

    def submit_results(self,results):
        print("submit results")
        pass


if __name__ == '__main__':
    
    with open("dataset/TREC2017-RTS-topics-final.json") as f:
        profiles=json.load(f)
        profile_title=profiles[0]['title']
        from extras import googleCSE as gcse
        expanded_title_by_google=gcse.expand_by_google(profile_title)
        print(expanded_title_by_google)
        profile =""

        # tl.test()
        # profiles[0]['description']
        # profiles[0]['title'] + " " + profiles[0]['description']
        # profiles[0]['narrative']


        # print(p[r])
        # pro=Processor()
        # pro.expand_query(query=)
        # pro.preprocess()