from processor import Processor
import time
import pymysql

class LocalListener:
    db = pymysql.connect("localhost", "root", "123", "trecrts")
    cursor = db.cursor()

    def __init__(self):
        pass
    #this a status by id which is used for debugging sometimes
    def get_status(self,id):
        sql = "select * from status where id = %s" % (id)
        try:
            self.cursor.execute(sql)
            results=self.cursor.fetchall()
        except:
            self.db.rollback()
            self.db.close()
        return results

    def get_train_status(self):
        pass

    # if there is no supervised machine learning algorithm appled, all status in database are used for testing
    def get_test_status(self):
        sql = "select * from status"
        self.cursor.execute(sql)
        try:
            self.cursor.execute(sql)
            results=self.cursor.fetchall()
        except:
            self.db.rollback()
            self.db.close()
        return results

    def listen(self,executor):
        executor.excute("listen tweet 1")
        # print("here is listenning local status")
        # test_status= self.get_test_status()
        # return test_status