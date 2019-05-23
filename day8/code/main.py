import pymysql
import settings
from dbhelper import db
from sign_on import sign_on
from sign_in import sign_in
from show_all import show_all

def main():
    conn = pymysql.Connection(**settings.parameters)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql_create_database = "create database bbs default charset=utf8;"
    sql_create_table = '''
    create table if not exists user(
    uid int primary key auto_increment,
    username VARCHAR(20) unique ,
    usertype enum('0','1') DEFAULT '0',
    password VARCHAR(40) not NULL ,
    regtime datetime ,
    email VARCHAR(30)
    )engine=innodb default charset=utf8;
    '''

    # cursor.execute(sql_create_database)
    conn.select_db("bbs")
    # cursor.execute(sql_create_table)


    sign_on()
    sign_in()
    show_all()


if __name__ == "__main__":
    main()