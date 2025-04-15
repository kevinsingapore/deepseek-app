#!/usr/bin/python3      

import os,yaml
from db import init
# 获取配置文件，读取配置文件参数
def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        return config



# 把warning与error的日志推送到rabbitmq