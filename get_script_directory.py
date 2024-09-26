# -*- utf-8 -*-
# @Create Data: 2024/4/23 17:17
# @Author: guangyang219579
# @File: get_script_directory.py

import os


def get_script_directory():
    """获取当前脚本所在的目录"""
    return os.path.dirname(os.path.abspath(__file__))
