#__author__ = 'unclepig'

import  dbcon_module

tb = 'user_category_cd_t'

uccode = input('코드는 무엇을 넣을까요? :')
ucname = input('코드명은 무엇이라고 할까요? :')


instparm = 'insert into '+ tb + ' ('
instparm = instparm + 'uc_code,'
instparm = instparm + 'uc_code_name,'
instparm = instparm + 'reg_user, reg_date'
instparm = instparm + ') values ('
instparm = instparm + "'"+ uccode + "',"
instparm = instparm + "'"+ ucname + "',"
instparm = instparm + "'unclepig',"
instparm = instparm + 'now());'

dbcon_module.udbinsert(instparm)

print(instparm)

