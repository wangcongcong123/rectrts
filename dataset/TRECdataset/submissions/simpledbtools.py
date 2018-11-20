import pymysql

db = pymysql.connect("localhost", "root", "123", "trecrts")
cursor = db.cursor()

def getAll2017Ids():
    sql = "select id from status where dataset_src like 'rts2017%'"
    cursor.execute(sql)
    results = cursor.fetchall()
    idlist=[]
    for each in results:
        idlist.append(each[0])
    closedb()
    return idlist

def closedb():
    cursor.close()
    db.close()
