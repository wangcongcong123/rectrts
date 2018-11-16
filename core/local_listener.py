from core.processor import Processor
import time
import pymysql

import timeit
class LocalListener:
    db = pymysql.connect("localhost", "root", "123", "trecrts")
    cursor = db.cursor()

    def __init__(self):
        pass

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
    def get_topn_status(self,n):
        sql = "select id,text,topic_label,relevance from status limit %d"%(n)
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

    def get_status_by_topiclist(self, topiclist):
        results=()
        for topic in topiclist:
            results+=self.get_status_by_topic(topic)
        return results

    def listen(self, executor):
        # print("here is listenning local status")
        with open("../dataset/log-tweetIds-in-db-2017-and-epoch.txt") as f:
            lines=f.readlines()
            count=0
            length_t=len(lines)
            for each in lines:
                start = timeit.default_timer()
                count+=1
                columns=each.strip().split()
                tweetid=columns[0]
                tweet=self.get_status_byId(tweetid)
                rebuild_tweet=(tweetid,columns[1],columns[2],tweet[0][6])
                # time.sleep(1)
                # print(rebuild_tweet)
                #rebuild_tweet format:
                #('891035114838294528', '20170728', '1501274300', 'Why are you like this???? @anakarendavilaa https://t.co/pbNHPb2MgO')
                executor.excute(rebuild_tweet)
                stop = timeit.default_timer()
                # print('Time: ', stop - start)
                print("Processing Tweet","(",length_t,")",count)

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
    pass
    # ll=LocalListener()
    # ll.listen()
    # print(len(ll.get_status_by_topiclist(["RTS46","RTS47"])))
    # locallistener.count()
