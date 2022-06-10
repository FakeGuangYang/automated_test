# -*- utf-8 -*-
# @Create Data: 2022/6/8 14:31
# @Author: guangyang219579
# @File: jina.py

from selenium.webdriver.common.by import By


# 集纳页元素
class Jina(object):
    def __init__(self, driver):
        self.driver = driver

    def find_channel_config_button(self):
        # find and return channel config button element
        ele = self.driver.find_element(By.CLASS_NAME, 'el-button el-button--default')
        return ele

    def find_new_channel_button(self):
        # find and return new channel button element
        ele = self.driver.find_element(By.CLASS_NAME, 'el-button el-button-primary')
        return ele

    def find_alter_button(self):
        # find and return alter button element
        ele = self.driver.find_element(By.CLASS_NAME, 'el-button el-button--primary el-button--mini')
        return ele

    def find_delete_button(self):
        # find and return delete button element
        ele = self.driver.find_element(By.CLASS_NAME,
                                       'el-button el-button--danger el-button--mini el-popover__reference')
        return ele

    def find_recommend_channel(self):
        # find and return recommend channel element
        ele = self.driver.find_element(By.ID, 'tab-1')
        return ele


# 集纳页操作
class JinaOper(object):
    def __init__(self, driver):
        self.login_page = Jina(driver)


# 集纳页场景
class JinaScenarios(object):
    def __init__(self, driver):
        self.login_oper = JinaOper(driver)
