import pymysql
import filetools as ft

db = pymysql.connect("localhost", "root", "123", "trecrts")
cursor = db.cursor()


#
# def getAll2017Ids():
#     sql = "select id from status where dataset_src like 'rts2017%'"
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     closedb()


def saveAllTIds():
    # sql = "select id from status"
    sql = "select id from status where dataset_src like 'rts2017%'"
    cursor.execute(sql)
    results = cursor.fetchall()
    length = len(results)
    count = 0
    id_str = ""
    for each in results:
        if count == length - 1:
            id_str += each[0]
        else:
            id_str += each[0] + "\n"
        count += 1
    closedb()
    ft.write_to_log("tweetIds-in-db-2017", id_str)
    print("finished obtaining all tweet ids form DB and write them to a file!")

def closedb():
    cursor.close()
    db.close()


def getAllTIdsFromFile(filename="log-tweetIds-in-db-2017.txt"):
    id_list = []
    id_dict = {}
    with open(filename, "r") as f:
        id_list = f.read().split("\n")
        for eachid in id_list:
            id_dict[eachid] = 0
    return id_dict


def getAllTIdsFromEpoch(filename):
    id_dict = {}
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            id_dict[line.strip().split()[0]]=0
    return id_dict

if __name__ == '__main__':
    # id_dict_2017 = getAllTIdsFromFile()
    # id_str_filtered = ""
    # with open("TRECdataset/rts2017-batch-tweets2dayepoch.txt", "r") as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         id = line.strip().split()[0]
    #         if id in id_dict_2017:
    #             id_str_filtered += line
    # ft.write_to_log("tweetIds-in-db-2017-and-epoch", id_str_filtered)
    # saveAllTIds()
    id_dict_epoch=getAllTIdsFromEpoch("log-tweetIds-in-db-2017-and-epoch.txt")
    id_str_filtered = ""
    group_submit_path="/IRIT/scenarioA/IRIT-Run3-A"
    with open("TRECdataset/submissions"+group_submit_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            id = line.strip().split()[1]
            if id in id_dict_epoch:
                id_str_filtered += line
    ft.write_to_file("TRECdataset/submissions"+group_submit_path+"-U", id_str_filtered)
    print("Update file to: ","TRECdataset/submissions"+group_submit_path+"-U")