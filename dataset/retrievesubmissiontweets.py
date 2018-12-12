import pymysql
import tweetapi
import filetools as ft
import time
import json
from pymysql import ProgrammingError, InternalError, IntegrityError
db = pymysql.connect("localhost", "root", "123", "trecrts")
cursor = db.cursor()
from tweepy import TweepError
if __name__ == '__main__':
    with open("TRECdataset/submissions/unqiue-submissions-tweetids-collection") as f:
        alllines = f.readlines()
    count = 0
    for line in alllines:
        eachid=line.strip()
        status_text = ""
        try:
            status = tweetapi.api.get_status(eachid, tweet_mode='extended')
        except TweepError as err:
            print(err)
            err_log = "\n" + eachid + "@TweepError:" + str(err)
            print(err.api_code)
            ft.write_to_log("get-full-2017-submissions", err_log)
            if err.api_code == None:
                print("sleeping 10 minutes due to the rate limit")
                time.sleep(10 * 60)
            continue
        status_json = status._json
        json_str = json.dumps(status._json)
        if "retweeted_status" in status_json:
            status_text = status_json['retweeted_status']['full_text']
        else:
            status_text = status_json['full_text']

        description = status.user.description
        loc = status.user.location
        coords = status.coordinates
        geo = status.geo
        name = status.user.screen_name
        user_created = status.user.created_at
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        retweets = status.retweet_count
        bg_color = status.user.profile_background_color
        sql = "INSERT INTO status(id,topic_label,relevance,user_description, user_location, coordinates, text,geo,user_name,user_created,user_followers,id_str,created,retweet_count,user_bg_color,dataset_src) VALUES" \
              " ('%s','%s','%d','%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%d' ,'%s','%s' )" % \
              (eachid, "None", -666, description.replace("\'", ""), loc.replace("\'", ""), coords,
               status_text.replace("\'", ""), geo, name.replace("\'", ""), user_created, followers, id_str, created, retweets,
               bg_color, "2017-all-submissions")
        print("process", count, " Tweet@", eachid)
        count += 1
        try:
            cursor.execute(sql)
            db.commit()
        except (ProgrammingError, InternalError, InternalError, IntegrityError) as err:
            err_log = "\n" + eachid + "@MYSQLError:" + str(err)
            print("\n" + eachid + "@MYSQLError:" + str(err))
            ft.write_to_log("get-full-2017-submissions", err_log)
            db.rollback()
db.close()