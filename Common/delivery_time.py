# -*- utf-8 -*-
# @Create Data: 2022/6/23 11:34
# @Author: guangyang219579
# @File: delivery_time.py

import datetime


# 计算发布时间
def delivery_time():
    end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    start_time = (datetime.datetime.now() - datetime.timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:%S')
    time = start_time + " - " + end_time
    return time
