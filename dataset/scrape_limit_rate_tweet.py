import time

import tweepy
from pymysql import ProgrammingError, InternalError, IntegrityError

import private
import pymysql
from tweepy import TweepError


def write_to_log(err_log):
    with open("err_log_rate_limit.txt", "a") as f:
        f.write(err_log)
    pass

def get_tweetIDs():
    tweetids={}
    with open("tweets-with-rate-limit.txt", "r") as f:
        alllines=f.read().split("\n")
        for each in alllines:
            tweetids[each]=1
    return tweetids


def main():
    auth = tweepy.OAuthHandler(private.TWITTER_APP_KEY, private.TWITTER_APP_SECRET)
    auth.set_access_token(private.TWITTER_KEY, private.TWITTER_SECRET)
    api = tweepy.API(auth)
    err_log = ""
    count = 0

    db = pymysql.connect("localhost", "root", "123", "trecrts")
    cursor = db.cursor()

    with open("TRECdataset/rts2017-mobile-qrels.txt",'r') as f:
        content=f.read().split("\n")
        print("the TRECdataset include %s lines (namely the number of tweets)"%(len(content)))
        alltweetids=get_tweetIDs()
        print(alltweetids)
        for eachline in content:
            attributes=eachline.split(" ")
            if attributes[1] not in alltweetids:
                continue
            status = ""
            try:
                status = api.get_status(attributes[1])
            except TweepError as err:
                print(err)
                err_log = "\n" + attributes[1] + "@TweepError:" + str(err)
                print(err.api_code)
                write_to_log(err_log)
                if err.api_code==None:
                    print("sleeping 10 minutes due to the rate limit")
                    time.sleep(10 * 60)
                continue

            id = status.id_str
            topiclabel=attributes[0]
            relevance=int(attributes[2])
            description = status.user.description
            loc = status.user.location
            text = status.text
            coords = status.coordinates
            geo = status.geo
            name = status.user.screen_name
            user_created = status.user.created_at
            followers = status.user.followers_count
            id_str = status.id_str
            created = status.created_at
            retweets = status.retweet_count
            bg_color = status.user.profile_background_color

            sql = "INSERT INTO status(id,topic_label,relevance,user_description, user_location, coordinates, text,geo,user_name,user_created,user_followers,id_str,created,retweet_count,user_bg_color) VALUES" \
                  " ('%s','%s','%d','%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%d' ,'%s' )" % \
                  (id, topiclabel,relevance,description.replace("\'",""), loc.replace("\'",""), coords,text.replace("\'",""),geo,name.replace("\'",""),user_created,followers,id_str,created,retweets,bg_color)
            print("process",count)
            count += 1
            try:
                cursor.execute(sql)
                db.commit()
            except (ProgrammingError,InternalError,InternalError,IntegrityError) as err:
                err_log="\n"+id+"@MYSQLError:"+str(err)
                print("\n"+id+"@MYSQLError:"+str(err))
                write_to_log(err_log)
                db.rollback

    db.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')



