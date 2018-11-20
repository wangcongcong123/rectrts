import timeit
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO
                    # ,handlers=[
                    #     # logging.FileHandler("{0}/{1}.log".format("/Users/wangcongcong/Desktop", "gensim")),
                    #     logging.StreamHandler()
                    # ]
                    )
import listener_designator
from processor import Processor
import logging

class Executor:
    def __init__(self):
        self.processor = Processor()
        pass

    def excute(self,tweet):
        self.processor.start(tweet)

if __name__ == '__main__':
    logging.info("-----Start Executing------")
    start = timeit.default_timer()
    executor = Executor()
    listener_designator.listen("local",executor)
    logging.info("-----End Executing------")
    stop = timeit.default_timer()
    logging.info('Time consumed: '+str(stop - start)+" seconds")


