#__author__ = 'unclepig'
import dbcon_module

tbname = input('테이블 명 :')
sqlwhere = input('where 절에 넣을 것은?')

dbsel = 'select * from ' + tbname

if sqlwhere != '' :
    dbsel = dbsel + ' where ' + sqlwhere
else :
        dbsel

print(dbsel)


dbcon_module.udbsel(dbsel)
