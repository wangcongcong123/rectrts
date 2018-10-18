
import listener_designator
from processor import Processor

class Executor:
    def __init__(self):
        self.processor = Processor()
        pass

    def excute(self,tweet):
        
        # ""
        self.processor.expand_query(" ")
        self.processor.preprocess(tweet)
        self.processor.compute_relevance(" "," ")
        self.processor.compute_redundancy(" "," ")
        self.processor.ranking(" ")






if __name__ == '__main__':
    executor =  Executor()
    listener_designator.listen("online",executor)

