# -*- utf-8 -*-
# @Create Data: 2022/5/21 15:15
# @Author: guangyang219579
# @File: parse_yml.py

import yaml
from get_script_directory import get_script_directory

"""
Parse yaml files through file name, section and key
"""


def parse_yml(file, section, key):
    with open(get_script_directory() + file, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data[section][key]
