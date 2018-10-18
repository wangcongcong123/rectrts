
from local_listener import LocalListener
from online_listener import  OnlineListener
import time
import settings
import tweepy
import dataset

def listen(option,executor):

    if option =="local":
        listener=LocalListener()
        listener.listen(executor)
    elif option=="online":
        print("online")
        auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET)
        auth.set_access_token(settings.TWITTER_KEY, settings.TWITTER_SECRET)
        api = tweepy.API(auth)
        stream_listener = OnlineListener()
        stream_listener.setExecutor(executor)
        stream= tweepy.Stream(auth=api.auth, listener=stream_listener)

        stream.filter(track=settings.TRACK_TERMS)
        # return OnlineListener()
    else:
        print("error, please give the option argument local or online")
