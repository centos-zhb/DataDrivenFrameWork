# encoding=utf-8
import MySQLdb
from Sql import *

class DataBaseInit(object):
    """
    本类用于完成初始化数据库操作
    创建数据库，创建数据表，向表中插入测试数据
    """
    def __init__(self,host,port,dbName,username,password,charset):
        self.host = host
        self.port = port
        self.db = dbName
        self.user = username
        self.passwd = password
        self.charset = charset

    def create(self):
        try:
            conn = MySQLdb.connect(
                host = self.host,
                port = self.port,
                user = self.user,
                passwd = self.passwd,
                charset = self.charset
            )
            # 获取数据库操作
            cur = conn.cursor()
            # 创建数据库
            cur.execute(create_database)
            # 选择创建好的数据库
            conn.select_db("gloryroad")
            cur.execute(create_table)
        except MySQLdb.Error ,e:
            raise e
        else:
            # 关闭游标
            cur.close()
            # 提交操作
            conn.commit()
            # 关闭连接
            conn.close()
            print u"创建数据库及表成功"

    def insertDatas(self):
        try:
            # 连接mysql中的具体某个库
            conn = MySQLdb.connect(
                host = self.host,
                port = self.port,
                db = self.db,
                user = self.user,
                passwd = self.passwd,
                charset = self.charset
            )
            cur = conn.cursor()
            # 向测试表中插入测试数据
            sql = 'insert into testdata(bookname,author) VALUES (%s,%s);'
            print "11111111111111111111111111111111"
            res = cur.executemany(sql,[('Selenium WebDriver实战宝典','吴晓华'),
                                       ('HTTP权威指南'),
                                       ('探索式软件测试','惠特克'),
                                       ('暗时间','刘未鹏')])
        except MySQLdb.Error,e:
            raise e
        else:
            conn.commit()
            print u'初始数据插入成功'
            cur.execute('select * from testdata;')
            for i in cur.fetchall():
                print i[1],i[2]
            cur.close()
            conn.close()

if __name__ == '__main__':
    db = DataBaseInit(
        host='139.199.28.210',
        port = 3306,
        dbName="gloryroad",
        username='root',
        password='zhb194236',
        charset='utf8'
    )
    db.create()
    db.insertDatas()
    print u"数据库初始化结束！"