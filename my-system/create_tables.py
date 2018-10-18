import pymysql
#open database
db = pymysql.connect("localhost","root","123","trecrts")
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS STATUS")
sql = """CREATE TABLE STATUS (
        id varchar(20) not null primary key,
        topic_label varchar(20),
        relevance integer,
        user_description varchar(200),
        user_location varchar(50),
        coordinates varchar(120),
        text varchar(320),
        geo varchar(120),
        user_name varchar(40),
        user_created varchar(60),
        user_followers varchar(240),
        id_str varchar(50),
        created varchar(40),
        retweet_count integer,
        user_bg_color varchar(10)
        )"""

cursor.execute(sql)
db.close()