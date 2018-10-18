
import tweepy

import private

auth = tweepy.OAuthHandler(private.TWITTER_APP_KEY, private.TWITTER_APP_SECRET)
auth.set_access_token(private.TWITTER_KEY, private.TWITTER_SECRET)
api = tweepy.API(auth)

status = api.get_status("890889671311601664")
