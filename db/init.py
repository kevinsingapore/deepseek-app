#!/usr/bin/python3

import pymysql

# 连接Mysql 
def  connect_to_mysql(configPath):
    config = {
        'host': configPath['database']['host'],
        'user': configPath['database']['user'],
        'password': configPath['database']['password'],
        'database': configPath['database']['database'],
        'charset': configPath['database']['charset'],
        'cursorclass': pymysql.cursors.DictCursor
    }
    
    try:
        conn = pymysql.connect(**config)
        print('成功连接到 MySQL 数据库!')
        return conn
    except Exception as e:
        print('连接 MySQL 数据库失败!')
        print(e)
        return None
    