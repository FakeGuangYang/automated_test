# -*- utf-8 -*-
# @Create Data: 2022/6/23 10:04
# @Author: guangyang219579
# @File: chrome_options.py

from selenium.webdriver.chrome.options import Options


# 在Linux运行时需要添加Chrome options
def chrome_options():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('blink-settings=imagesEnabled=false')
    return options
