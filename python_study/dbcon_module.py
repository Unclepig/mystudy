#__author__ = 'unclepig'

import pymysql

def udbconnection(con, sql):
    dbcon = pymysql.Connect(con, port=3306,user='root',passwd='samsam',db='mydb')
    dbcur = dbcon.cursor()
    dbcur.execute(sql)
    return dbcur
    dbcur.close()
    dbcon.close()

def udbinsert(insql) :
    udbcon = pymysql.Connect('localhost',port=3306,user='root',passwd='samsam',db='mydb', autocommit=True,charset='utf8')
    udbcur = udbcon.cursor()
    try:
        udbcur.execute(insql)
        return 1
    except :
        return 0
    udbcur.close()
    udbcon.close()

def udbsel(selsql):
    selcon = pymysql.Connect('localhost',port=3306,user='root',passwd='samsam',db='mydb', autocommit=True,charset='utf8')
    selcur = selcon.cursor()
    selcur.execute(selsql)
    for row in selcur:
        print(row)
    selcur.close()
    selcon.close()





