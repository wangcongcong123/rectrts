import timeit
import logging



logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO
                    # ,handlers=[
                    #     # logging.FileHandler("{0}/{1}.log".format("/Users/wangcongcong/Desktop", "gensim")),
                    #     logging.StreamHandler()
                    # ]
                    )
from core import listener_designator
from core.processor import Processor
import logging
from core import configfile

class Executor:
    def __init__(self):
        self.processor = Processor()
        pass

    def excute(self, tweet):
        self.processor.start(tweet)

def execute():
    logging.info("-----Start Executing------")
    start = timeit.default_timer()
    executor = Executor()
    listener_designator.listen(configfile.MODE, executor)
    logging.info("-----End Executing------")
    stop = timeit.default_timer()
    logging.info('Time consumed: ' + str(stop - start) + " seconds")

