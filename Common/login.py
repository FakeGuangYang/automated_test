# -*- utf-8 -*-
# @Create Data: 2022/7/12 15:59
# @Author: guangyang219579
# @File: login.py

from Common.parse_yml import parse_yml
from Test.PageObject import login_page

# 登录页url
login_url = parse_yml("/Config/login.yml", 'websites', 'loginPage')
# 登录信息
username = parse_yml("/Config/login.yml", 'loginInfo', 'username')
password = parse_yml("/Config/login.yml", 'loginInfo', 'password')


def login(driver):
    driver.get(login_url)
    # 登录
    login_page.LoginScenarios(driver).login(username, password)
