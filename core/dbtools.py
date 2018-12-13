import json

import pymysql
from pymysql import IntegrityError

db = pymysql.connect("localhost", "root", "123", "trecrts")
cursor = db.cursor()

def status2db(status):
    description = status.user.description
    loc = status.user.location
    coords = status.coordinates
    geo = status.geo
    name = status.user.screen_name
    user_created = status.user.created_at
    followers = status.user.followers_count
    created = status.created_at
    retweets = status.retweet_count
    bg_color = status.user.profile_background_color
    strid=status.id_str
    text=status.text
    sql = "INSERT INTO listenpool(id,topic_label,relevance,user_description, user_location, coordinates, text,geo,user_name,user_created,user_followers,id_str,created,retweet_count,user_bg_color,dataset_src) VALUES" \
          " ('%s','%s','%d','%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%d' ,'%s','%s' )" % \
          (strid, "None", -666, description.replace("\'", ""), loc.replace("\'", ""), coords,
           text.replace("\'", ""), geo, name.replace("\'", ""), user_created, followers, strid, created,
           retweets,
           bg_color, "online-listen")
    try:
        cursor.execute(sql)
    except:
        db.rollback()
        db.close()

def status2dbbatch(statusbatch):
    # for status in status2dbbatch:
    #     status2db(status)
    connection = pymysql.connect("localhost", "root", "123", "trecrts")
    try:
        with connection.cursor() as cursor:
            for status in statusbatch:
                description = status.user.description
                loc = status.user.location
                coords = status.coordinates
                geo = status.geo
                name = status.user.screen_name
                user_created = status.user.created_at
                followers = status.user.followers_count
                created = status.created_at
                retweets = status.retweet_count
                bg_color = status.user.profile_background_color
                strid = status.id_str
                # text = status.text
                description="" if description==None else description
                loc = ""
                name = ""
                status_text=""
                status_json = status._json
                if "retweeted_status" in status_json:
                    status_text = status_json['retweeted_status']['text']
                else:
                    status_text = status_json['text']
                # print(status)
                if "\\" in description:
                    description.replace("\\","")
                if "\\" in status_text:
                    status_text.replace("\\","")
                # geo=None if geo!=None else None
                # Create a new record
                sql = "INSERT INTO listenpool(id,topic_label,relevance,user_description, user_location, coordinates, text,geo,user_name,user_created,user_followers,id_str,created,retweet_count,user_bg_color,dataset_src) VALUES" \
                      " ('%s','%s','%d','%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%s' ,'%d' ,'%s','%s' )" % \
                      (strid, "None", -666, description.replace("\'", ""), "None", "None",
                       status_text.replace("\'", ""), "None", name.replace("\'", ""), user_created, followers, strid, created,
                       retweets,
                       bg_color, "online-listen")
                try:
                    cursor.execute(sql)
                    connection.commit()
                except IntegrityError as err:
                    print(err)
                    # connection.rollback()
            print("Finished save ",len(statusbatch)," status")
    finally:
        connection.close()
