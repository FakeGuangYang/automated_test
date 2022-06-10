# -*- utf-8 -*-
# @Create Data: 2022/5/21 15:13
# @Author: guangyang219579
# @File: parse_csv.py

import csv


def parse_csv(file):
    mylist = []
    with open(file, 'r', encoding='utf-8') as f:
        data = csv.reader(f)
        for i in data:
            mylist.append(i)
        return mylist[1:]
