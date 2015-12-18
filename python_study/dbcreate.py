#__author__ = 'unclepig'

import dbcon_module

ucon = 'localhost'

# create_sql = 'create table useful_text ('
# create_sql = create_sql + 'ut_seq int not null auto_increment primary key,'
# create_sql = create_sql + 'uc_code varchar(45) not null,'
# create_sql = create_sql + 'reg_user varchar(45) not null,'
# create_sql = create_sql + 'ut_content text,'
# create_sql = create_sql + 'ut_tag text,'
# create_sql = create_sql + 'ut_reg_date date'
# create_sql = create_sql + ')'

create_sql = 'create table user_category_cd_t ('
create_sql = create_sql +'uc_code_seq int not null auto_increment primary key,'
create_sql = create_sql +'uc_code varchar(45) not null,'
create_sql = create_sql +'uc_code_name varchar(45) not null,'
create_sql = create_sql +'reg_user varchar(45) not null,'
create_sql = create_sql +'reg_date date not null'
create_sql = create_sql + ')'


dbcon_module.udbconnection(ucon,create_sql)

print(create_sql)