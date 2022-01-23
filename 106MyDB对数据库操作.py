'''
操作SQLite数据库
轻量级数据库
'''
# 数据库下载
# https://sqlitebrowser.org/dl/

import sys
# QSqlDatabase：用来操作数据库
# QSqlQuery：
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

def createDB():
    # 本地数据库不需要提供账号密码，只需要提供本地的文件名
    # 实例化数据库 ，addDatabase('QSQLITE')添加数据库种类为SQLite数据库
    db = QSqlDatabase.addDatabase('QSQLITE')
    # 指定SQLite数据库的文件名
    db.setDatabaseName('./database.db')
    # 如果无法打开，输出下面文案
    if not db.open():
        print('无法建立与数据库的连接')
        return False
    # 创建一个空的数据库文件
    query = QSqlQuery()
    query.exec('create table people(id int primary key,name varchar(10),address varchar(50))')
    query.exec('insert into people values(1,"李宁","Shenyang")')
    query.exec('insert into people values(2,"超人","克星")')
    db.close()
    return True

if __name__ == '__main__':
    createDB()