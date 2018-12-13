import timeit

from core.local_listener import LocalListener
from core.online_listener import OnlineListener
import settings
import tweepy

def listen(option, executor):
    if option == "local":
        listener = LocalListener()
        listener.listen(executor)
    elif option == "online":
        auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET)
        auth.set_access_token(settings.TWITTER_KEY, settings.TWITTER_SECRET)
        api = tweepy.API(auth)
        stream_listener = OnlineListener()
        stream_listener.setParaUp(executor)
        stream = tweepy.Stream(auth=api.auth, listener=stream_listener,tweet_mode='extended')
        # stream.filter(track=["china"])
        # stream.filter(languages=["en"])
        stream.sample()
        # stream.sample()
        # return OnlineListener()
    else:
        print("error, please give the option argument local or online")

if __name__ == '__main__':
    listen("online",None)
    stop = timeit.default_timer()

