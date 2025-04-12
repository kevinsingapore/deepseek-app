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
init.connect_to_mysql(config)


# monitor.get_log(logPath)

