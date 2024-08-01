# -*- utf-8 -*-
# @Create Data: 2024/5/10 14:27
# @Author: guangyang219579
# @File: added_account_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# 已添加用户页对象
class AddedAccountPage(object):
    def __init__(self, driver):
        self.driver = driver

    """
    以下为已添加账号页面中的元素
    """

    # "帐号昵称"搜索框元素
    def find_name_input(self):
        ele = self.driver.find_element(By.ID, 'name')
        return ele

    # [搜索]按钮元素
    def find_search_button(self):
        ele = self.driver.find_element(By.ID, 'search')
        return ele


# 已添加用户页操作
class AddedAccountOper(object):
    def __init__(self, driver):
        self.added_account_page = AddedAccountPage(driver)
        self.wait = WebDriverWait(driver, 100)

    """
    以下操作用于场景中，模拟用户操作
    """

    # 在帐号昵称输入框输入帐号昵称
    def input_name(self, name):
        self.added_account_page.find_name_input().clear()
        self.added_account_page.find_name_input().send_keys(name)

    # 点击[搜索]按钮
    def click_search_button(self):
        self.added_account_page.find_search_button().click()


# 已添加用户页场景
class AddedAccountScenarios(object):
    def __init__(self, driver):
        self.added_account_oper = AddedAccountOper(driver)

    # 搜索一个帐号昵称
    def search_name(self, name):
        self.added_account_oper.input_name(name)
        self.added_account_oper.click_search_button()
