# encoding=utf-8

# 创建gloryroad数据库SQL语句
create_database = 'CREATE DATABASE IF NOT EXISTS gloryroad DEFAULT CHARSET utf8 COLLATE utf8_general_ci;'

# 创建testdata表
create_table = """
    drop table if EXISTS testdata;
    CREATE TABLE testdata(
      id int not null auto_increment comment '主键',
      bookname VARCHAR(40) UNIQUE not null comment '书名',
      author VARCHAR(30) NOT NULL comment '作者',
      PRIMARY KEY (id)
    ) engine = innodb character set utf8 comment '测试数据库'
"""