#!/user/env/bin python3
#-*- coding:utf-8 -*-

#导入sqlite驱动
import sqlite3


#连接到SQLite数据库
#数据库的文件是test.db
conn = sqlite3.connect('test.db')

#创建一个Curser
cursor = conn.cursor()

#创建user表
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

#插入一条记录
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

print(cursor.rowcount)
#执行查询语句
cursor.execute('select * from user where id=?', ('1',))
#获得查询结果
values = cursor.fetchall()
print(values)
# 关闭Cursor:
cursor.close()
# 关闭Connection:
conn.close()