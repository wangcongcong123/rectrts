import oauth2
import tweepy

import private
import json

#
class OnlineListener(tweepy.StreamListener):
    def setExecutor(self, executor):
        self.executor = executor

    def on_status(self, status):
        if status.retweeted:
            return

        # status_json = status._json
        # json_str = json.dumps(status._json)
        # # print(status)
        # if hasattr(status, "retweeted_status"):
        #     if hasattr(status, "extended_tweet"):
        #         print("extednded", status.retweeted_status.extended_tweet)
        #     else:
        #         print("not extednded", status.text)
        # # print(json.dump(status))
        #
        # else:
        json_str = json.dumps(status._json)
        status_json = status._json
        if "extended_tweet" in status_json:
            print(status_json['extended_tweet']['full_text'])
        elif 'retweeted_status' in status_json:
            if 'extended_tweet' in status_json['retweeted_status']:
                print(status_json['retweeted_status']['extended_tweet']['full_text'])
            else:
                print(status_json['text'])
        else:
            print(status_json['text'])
        print(status_json['id'])

        # if hasattr(status,'extended_tweet'):
        #     print("included")
        #     print(status.id,status.extended_tweet['full_text'])
        # else: print(status.id,status.text)
        print("-------------------------------------------------")
        # if 'extended_text' in status:
        #     print(status.text)
        # else: print(status.extended_text.full_text)

        # print("get a tweet",status)
        # self.executor.excute(status)

    def on_error(self, status_code):
        if status_code == 420:
            return False


auth = tweepy.OAuthHandler(private.TWITTER_APP_KEY, private.TWITTER_APP_SECRET)
auth.set_access_token(private.TWITTER_KEY, private.TWITTER_SECRET)
api = tweepy.API(auth)

status = api.get_status("891085765232525314", tweet_mode='extended')
print(status)
status_json=status._json
json_str = json.dumps(status._json)
print(json_str)
if "retweeted_status" in status_json:
    print(status_json['retweeted_status']['full_text'])
else: print(status_json['full_text'])


# if hasattr(status,'retweeted_status'):
#     print(status.retweeted_status['full_text'])

# status = api.get_status("1060676114090221568")
# print(status)
#
# json_str = json.dumps(status._json)
# print(json_str)
# stream_listener = OnlineListener()
# # stream_listener.setExecutor(executor)
# stream = tweepy.Stream(auth=api.auth, listener=stream_listener, tweet_mode='extended')
# # stream.filter(track=["china"])
# # stream.filter(languages=["en"])
# stream.sample(languages=["en"])

CONSUMER_KEY = "735080426956431360-ZQIvRorrq9cESFeGlGNvcbq0h5HSaOC"
CONSUMER_SECRET = "axPUNtBCnkSE762iFPlgvGTfcfrelAf96kJaq2HCggGNQ"
TWITTER_APP_KEY = "fldVf72UB39XbqdzUAPN7UusR"
TWITTER_APP_SECRET = "IsS82Is9wAivJnqjsWvqP2kgikpq2VUD7QQiZVg4OvwfIMIICj"

# import twitter
# api = twitter.Api(consumer_key=CONSUMER_KEY,
#   consumer_secret=CONSUMER_SECRET,
#   access_token_key=TWITTER_APP_KEY,
#   access_token_secret=TWITTER_APP_SECRET)
#
# print(api.GetStatus(210462857140252672))
# def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
#     consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
#     token = oauth2.Token(key=key, secret=secret)
#     client = oauth2.Client(consumer, token)
#     resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
#     return content
#
#
# home_timeline = oauth_req('https://api.twitter.com/1.1/statuses/show.json?id=210462857140252672', TWITTER_APP_KEY,
#                           TWITTER_APP_SECRET)
