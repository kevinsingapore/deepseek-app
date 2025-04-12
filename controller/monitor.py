#!/usr/bin/python3      

import os,yaml

# 获取配置文件，读取配置文件参数
def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        return config

# 获取日志，读取日志，增量读取日志 
def get_log(log_path):
    if os.path.exists(log_path):
        with open(log_path, 'r') as file:
            lines = file.readlines()
            # return log
            for line in lines: 
                # 如果line内容中包含warning或error，则推送到mysql与rabbtimq中               
                if "warning" in line or "error" in line:
                    # 推送到mysql
                    
                    # 推送到rabbitmq中
                    print("推送到mysql与rabbitmq中")
    else:
        print("日志文件不存在")

# 把warning与error的日志推送到rabbitmq