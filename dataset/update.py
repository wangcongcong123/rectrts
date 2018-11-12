import pymysql
import tweetapi
import filetools as ft
import time
import json
from pymysql import ProgrammingError, InternalError, IntegrityError

db = pymysql.connect("localhost", "root", "123", "trecrts")
cursor = db.cursor()
# sql = "select id,topic_label, length(text),text from  status where text like '%…%' and length(text)>=140"
# cursor.execute(sql)
# results = cursor.fetchall()
# import pprint
# pprint.pprint(len(results))
# for each in results:
#     tweetid=each[0]
#     ft.write_to_log("tweets-to-update",tweetid+"\n")
from tweepy import TweepError
with open("log-tweets-to-update.txt") as f:
    content=f.read()
    tweetidstoupdate=content.split("\n")
    count=0
    for eachid in tweetidstoupdate:
        status_text=""
        try:
            status = tweetapi.api.get_status(eachid, tweet_mode='extended')
        except TweepError as err:
            print(err)
            err_log = "\n" + eachid + "@TweepError:" + str(err)
            print(err.api_code)
            ft.write_to_log("get-full-tweet",err_log)
            if err.api_code == None:
                print("sleeping 10 minutes due to the rate limit")
                time.sleep(10 * 60)
            continue
        status_json = status._json
        json_str = json.dumps(status._json)
        if "retweeted_status" in status_json:
            status_text=status_json['retweeted_status']['full_text']
        else:
            status_text=status_json['full_text']
        sql = "update status set text='%s' where id='%s'"%(status_text.replace("\'",""),eachid)
        print("process", count," Tweet@",eachid)
        count += 1
        try:
            cursor.execute(sql)
            db.commit()
        except (ProgrammingError, InternalError, InternalError, IntegrityError) as err:
            err_log = "\n" + eachid + "@MYSQLError:" + str(err)
            print("\n" + eachid + "@MYSQLError:" + str(err))
            ft.write_to_log("get-full-tweet", err_log)
            db.rollback()
db.close()

#


#

# print(status)



