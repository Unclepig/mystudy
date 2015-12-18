# __author__ = 'unclepig'

print("my world")

import pymysql

conn = pymysql.Connect(host='localhost',port=3306,user='root', passwd='samsam', db='mydb',autocommit=True,charset='utf8')
cur = conn.cursor()
cur.execute("select * from code_t")

for row in cur:
    print('samsamsam\n',row)

cur.close()
conn.close()



