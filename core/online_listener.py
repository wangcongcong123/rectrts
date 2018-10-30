import tweepy

class OnlineListener(tweepy.StreamListener):
    def setExecutor(self,executor):
        self.executor=executor

    def on_status(self, status):
        if status.retweeted:
            return
        # print("get a tweet",status)
        self.executor.excute(status)
    def on_error(self, status_code):
        if status_code == 420:
            return False
