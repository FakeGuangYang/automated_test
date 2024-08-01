# -*- utf-8 -*-
# @Create Data: 2024/5/9 11:29
# @Author: guangyang219579
# @File: new_user_news_delivery_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


# 新用户文章投放页对象
class NewUserNewsDeliveryPage(object):
    def __init__(self, driver):
        self.driver = driver

    """
    以下为新用户文章投放页面中的元素
    """

    # "oid"搜索框元素
    def find_oid_input(self):
        ele = self.driver.find_element(By.ID, 'oid')
        return ele

    # [搜索]按钮元素
    def find_search_content_button(self):
        ele = self.driver.find_element(By.ID, 'search_content')
        return ele

    # [投放]按钮元素
    def find_delivery_content_button(self):
        ele = self.driver.find_element(By.ID, 'delivery_content')
        return ele

    """
    以下为投放弹窗中的元素
    """

    # "oid"输入框元素
    def find_new_oid_input(self):
        ele = self.driver.find_element(By.ID, 'new_oid')
        return ele

    # "权重"输入框元素
    def find_new_weight_input(self):
        ele = self.driver.find_element(By.ID, 'new_weight')
        return ele

    # "投放时间"输入框元素
    def find_delivery_time_input(self):
        ele = self.driver.find_element(By.ID, 'delivery_time')
        return ele

    # [确认]按钮元素
    def find_save_button(self):
        ele = self.driver.find_element(By.ID, 'save')
        return ele

    # 弹窗[确定]按钮元素
    def find_submit_button(self):
        ele = self.driver.find_element(By.XPATH, '//button[contains(.,"确定")]')
        return ele


# 新用户文章投放页操作
class NewUserNewsDeliveryOper(object):
    def __init__(self, driver):
        self.new_user_news_delivery_page = NewUserNewsDeliveryPage(driver)
        self.wait = WebDriverWait(driver, 100)

    """
    以下操作用于场景中，模拟用户操作
    """

    # 点击[添加]按钮
    def click_delivery_content_button(self):
        self.new_user_news_delivery_page.find_delivery_content_button().click()

    # 在oid输入框输入oid
    def input_new_oid(self, oid):
        self.new_user_news_delivery_page.find_new_oid_input().clear()
        self.new_user_news_delivery_page.find_new_oid_input().send_keys(oid)

    # 在权重输入框输入权重
    def input_new_weight(self, weight):
        self.new_user_news_delivery_page.find_new_weight_input().clear()
        self.new_user_news_delivery_page.find_new_weight_input().send_keys(weight)

    # 在投放时间输入框输入投放时间
    def input_delivery_time(self, delivery_time):
        self.new_user_news_delivery_page.find_delivery_time_input().clear()
        self.new_user_news_delivery_page.find_delivery_time_input().send_keys(delivery_time)

    # 点击[确认]按钮
    def click_save_button(self):
        self.new_user_news_delivery_page.find_save_button().click()

    # 点击弹窗[确定]按钮
    def click_submit_button(self):
        self.new_user_news_delivery_page.find_submit_button().click()


# 新用户文章投放页场景
class NewUserNewsDeliveryScenarios(object):
    def __init__(self, driver):
        self.new_user_news_delivery_oper = NewUserNewsDeliveryOper(driver)

    # 增加一条新数据
    def add_new_oid(self, oid, weight, delivery_time):
        self.new_user_news_delivery_oper. click_delivery_content_button()
        self.new_user_news_delivery_oper.input_new_oid(oid)
        self.new_user_news_delivery_oper.input_new_weight(weight)
        self.new_user_news_delivery_oper.input_delivery_time(delivery_time)
        sleep(3)
        self.new_user_news_delivery_oper.click_save_button()
        sleep(2)
        self.new_user_news_delivery_oper.click_submit_button()
