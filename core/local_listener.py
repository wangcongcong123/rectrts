# from core.processor import Processor
import time
import datetime
import pymysql
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO
                    # ,handlers=[
                    #     # logging.FileHandler("{0}/{1}.log".format("/Users/wangcongcong/Desktop", "gensim")),
                    #     logging.StreamHandler()
                    # ]
                    )
import timeit
import core.configfile as configfile

class LocalListener:
    db = pymysql.connect("localhost", "root", "123", "trecrts")
    cursor = db.cursor()

    def __init__(self):
        self.simulated_collection = []
        results = ()
        if configfile.DB_SRC == "listenpool":
            results = LocalListener.get_listenpool()
        elif configfile.DB_SRC == "status":
            results = LocalListener.get_status_2017()
        for each in results:
            created_time = each[4]
            # timestamp_ = time.mktime(datetime.datetime.strptime(created_time, "%Y-%m-%d %H:%M:%S").timetuple())
            # 2017-08-04 03:02:39
            reformattime = created_time.split()[0].split("-")[1] + created_time.split()[0].split("-")[2] + "-" + \
                           created_time.split()[1]
            rebuild_tweet = (each[0], created_time.split()[0].replace("-", ""), reformattime, each[1])



            self.simulated_collection.append(rebuild_tweet)
        self.length_t = len(self.simulated_collection)

    # this a status by id which is used for debugging sometimes
    def get_status_byId(self, id):
        sql = "select * from status where id = %s" % (id)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except:
            self.db.rollback()
            self.db.close()
        return results

    def get_status_byIdlist(self, id_list):
        sql = "select * from status where id in %s" % (id_list)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except:
            self.db.rollback()
            self.db.close()
        return results

    def get_train_status(self):
        pass

    # if there is no supervised machine learning algorithm appled, all status in database are used for testing
    def get_test_status(self):
        sql = "select * from status order by topic_label"
        self.cursor.execute(sql)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except:
            self.db.rollback()
            self.db.close()
        return results

    # this method is used for playing around with tweets in small volumns
    def get_topn_status(self, n):
        sql = "select id,text,topic_label,relevance from status limit %d" % (n)
        self.cursor.execute(sql)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except:
            self.db.rollback()
            self.db.close()
        return results

    # this method is used for playing around with tweets in small volumns
    def get_status_by_topic(self, tl):
        sql = "select id,text,topic_label,relevance from status where topic_label = '%s'" % (tl)
        self.cursor.execute(sql)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except:
            self.db.rollback()
            self.db.close()
        return results

    # select count(*) from status where dataset_src like "rts2017%"
    @classmethod
    def get_status_2017(cls):
        sql = "select id,text,topic_label,relevance,created from status where dataset_src like %s" % (
                "'" + "rts2017%" + "'")
        results = ()
        try:
            cls.cursor.execute(sql)
            results = cls.cursor.fetchall()
        except:
            cls.db.rollback()
            cls.db.close()
        return results

    @classmethod
    def get_listenpool(cls):
        sql = "select id,text,topic_label,relevance,created from listenpool"
        results = ()
        try:
            cls.cursor.execute(sql)
            results = cls.cursor.fetchall()
        except:
            cls.db.rollback()
            cls.db.close()
        return results

    def get_status_by_topiclist(self, topiclist):
        results = ()
        for topic in topiclist:
            results += self.get_status_by_topic(topic)
        return results

    def listen(self, executor):
        # results=self.get_status_2017()
        # for each in results:
        count = 0
        for rebuild_tweet in self.simulated_collection:
            count += 1
            # print(rebuild_tweet)
            executor.excute(rebuild_tweet)
            logging.info("Processing Tweet" + "(" + str(self.length_t) + ")" + str(count))
        # print("here is listenning local status")
        # with open("../dataset/log-tweetIds-in-db-2017-and-epoch.txt") as f:
        #     lines=f.readlines()
        #     count=0
        #     length_t=len(lines)
        #     for each in lines:
        #         start = timeit.default_timer()
        #         count+=1
        #         columns=each.strip().split()
        #         tweetid=columns[0]
        #         tweet=self.get_status_byId(tweetid)
        #         rebuild_tweet=(tweetid,columns[1],columns[2],tweet[0][6])
        #         # time.sleep(1)
        #         # print(rebuild_tweet)
        #         #rebuild_tweet format:
        #         #('891035114838294528', '20170728', '1501274300', 'Why are you like this???? @anakarendavilaa https://t.co/pbNHPb2MgO')
        #         executor.excute(rebuild_tweet)
        #         stop = timeit.default_timer()
        #         # print('Time: ', stop - start)
        #         print("Processing Tweet","(",length_t,")",count)

    def count(self):
        count_dic = {}
        # not relevant
        count_dic[0] = 0
        # relevant
        count_dic[1] = 0
        # redundant
        count_dic[2] = 0
        count_dic[5] = 0
        # print("here is listenning local status")
        test_status = self.get_test_status()
        for each in test_status:
            # print(each[2])
            count_dic[each[2]] += 1
        #     if each[2] in count_dic.keys():
        #         count_dic[each[2]]=1
        #     else:
        #         count_dic[each[2]] += 1
        print(count_dic)


if __name__ == '__main__':
    # pass
    # ll = LocalListener()
    # ll.listen()

    results = LocalListener.get_listenpool()
    print(results)
    # results=ll.get_status_byIdlist(str(("760265746425479168","891688738383953922"))+"")
    # print(results)
    # for each in results:
    #     created_time=each[12]
    #     timestamp_=time.mktime(datetime.datetime.strptime(created_time, "%Y-%m-%d %H:%M:%S").timetuple())
    #     rebuild_tweet = (each[0], created_time.split()[0].replace("-",""), int(timestamp_), each[6])
    #     print(rebuild_tweet)
    # ll.listen()
    # print(len(ll.get_status_by_topiclist(["RTS46","RTS47"])))
    # locallistener.count()
