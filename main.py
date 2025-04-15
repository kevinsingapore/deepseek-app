#!/usr/bin/python3

import os
from  controller import monitor
from db import init


# 读取配置文件
config = monitor.load_config('config.yaml')
print('config:',config)

# 获取日志路径
logPath = os.getcwd() + '/' + str(config['logPath'][0])
print(logPath)


# 初始化连接 MySQL数据库
conn = init.connect_to_mysql(config)
cursor = conn.cursor()


# monitor.get_log(logPath)
# 获取日志，读取日志，增量读取日志 
def get_log(log_path,conn):
    if os.path.exists(log_path):
        with open(log_path, 'r') as file:
            lines = file.readlines()
            # return log
            for line in lines: 
                # 如果line内容中包含warning或error，则推送到mysql与rabbtimq中               
                if "warning" in line or "error" in line:
                    # 推送到mysql
                    sqlStr = "INSERT INTO messages (content) VALUES (%s)"
                    cursor.execute(sqlStr, (line.strip()))
                    conn.commit()
                    
                    # 推送到rabbitmq中
                    # print("推送到rabbitmq中")
    else:
        print("日志文件不存在")
        
get_log(logPath,conn)

