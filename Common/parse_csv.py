# -*- utf-8 -*-
# @Create Data: 2022/5/21 15:13
# @Author: guangyang219579
# @File: parse_csv.py

import csv
from get_script_directory import get_script_directory


def parse_csv(file):
    mylist = []
    with open(get_script_directory() + file, 'r', encoding='utf-8') as f:
        data = csv.reader(f)
        for i in data:
            mylist.append(i)
        return mylist[1:]
