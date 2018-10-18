import settings
import tweepy
import dataset
from textblob import TextBlob
from sqlalchemy.exc import ProgrammingError
import json

# db = dataset.connect(settings.CONNECTION_STRING)

class OnlineListener(tweepy.StreamListener):

    # def __init__(self,executor):
    #     self.executor=executor
    #     pass

    def setExecutor(self,executor):
        self.executor=executor

    def on_status(self, status):
        if status.retweeted:
            return
        print("get a tweet",status)
        self.executor.excute(status)
        # description = status.user.description
        # loc = status.user.location
        # text = status.text
        # coords = status.coordinates
        # geo = status.geo
        # name = status.user.screen_name
        # user_created = status.user.created_at
        # followers = status.user.followers_count
        # id_str = status.id_str
        # created = status.created_at
        # retweets = status.retweet_count
        # bg_color = status.user.profile_background_color
        # blob = TextBlob(text)
        # sent = blob.sentiment
        #
        # if geo is not None:
        #     geo = json.dumps(geo)
        #
        # if coords is not None:
        #     coords = json.dumps(coords)
        # table = db[settings.TABLE_NAME]
        #
        # try:
        #     table.insert(dict(
        #         user_description=description,
        #         user_location=loc,
        #         coordinates=coords,
        #         text=text,
        #         geo=geo,
        #         user_name=name,
        #         user_created=user_created,
        #         user_followers=followers,
        #         id_str=id_str,
        #         created=created,
        #         retweet_count=retweets,
        #         user_bg_color=bg_color,
        #         polarity=sent.polarity,
        #         subjectivity=sent.subjectivity,
        #     ))
        # except ProgrammingError as err:
        #     print(err)

    def on_error(self, status_code):
        if status_code == 420:
            return False

# if __name__ == '__main__':
#     auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET)
#     auth.set_access_token(settings.TWITTER_KEY, settings.TWITTER_SECRET)
#     api = tweepy.API(auth)
#
#     stream_listener = StreamListener()
#     stream_listener.setExecutor(executor)
#
#     stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
#     stream.filter(track=settings.TRACK_TERMS)