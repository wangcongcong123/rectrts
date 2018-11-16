
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
    import timeit
    print("-----Start Executing------")
    start = timeit.default_timer()
    executor = Executor()
    listener_designator.listen("local",executor)
    print("-----End Executing------")
    stop = timeit.default_timer()
    print('Time: ', stop - start)

