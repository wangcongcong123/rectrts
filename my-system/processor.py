
class Processor:
    def __init__(self):
        pass

    def expand_query(self,query):
        print("this is expand_query class")
        pass

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