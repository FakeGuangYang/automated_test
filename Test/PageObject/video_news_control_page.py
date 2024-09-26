# -*- utf-8 -*-
# @Create Data: 2022/7/8 11:12
# @Author: guangyang219579
# @File: video_news_control_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

sleep_time = 4


# 视频监控页对象
class VideoNewsControlPage(object):
    def __init__(self, driver):
        self.driver = driver

    """
    以下为视频监控页面搜索区域中的元素
    """

    # "oid搜索框"元素
    def find_search_oid_input(self):
        ele = self.driver.find_element(By.ID, 'oid')
        return ele

    # "[搜索]"按钮元素
    def find_search_content_button(self):
        ele = self.driver.find_element(By.ID, 'search')
        return ele

    """
    以下为视频监控列表区域中的元素
    """

    # 列表"oid"元素
    def find_table_oid(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="29540815"]/td[1]')
        return ele

    # 列表"[投放]"按钮元素
    def find_table_delivery_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="29540815"]/td[9]/div/button')
        return ele

    """
    以下为视频监控投放弹窗中的元素
    """

    # 弹窗"投放时间"元素
    def find_put_time_input(self):
        ele = self.driver.find_element(By.ID, 'put_time')
        return ele

    # 弹窗"[确认]"按钮元素
    def find_submit_button(self):
        ele = self.driver.find_element(By.ID, 'submit_check')
        return ele


# 视频监控页操作
class VideoNewsControlOper(object):
    def __init__(self, driver):
        self.video_news_control_page = VideoNewsControlPage(driver)
        self.wait = WebDriverWait(driver, 100)

    """
    以下操作用于场景中，模拟用户操作
    """

    # 输入oid
    def input_oid(self, oid):
        self.video_news_control_page.find_search_oid_input().clear()
        self.video_news_control_page.find_search_oid_input().send_keys(oid)

    # 点击[搜索]按钮
    def click_search_button(self):
        self.video_news_control_page.find_search_content_button().click()

    # 点击[投放]按钮
    def click_delivery_button(self):
        self.video_news_control_page.find_table_delivery_button().click()

    # 输入投放时间
    def input_put_time(self, put_time):
        self.video_news_control_page.find_put_time_input().clear()
        self.video_news_control_page.find_put_time_input().send_keys(put_time)

    # 点击[确认]按钮
    def click_submit_button(self):
        self.video_news_control_page.find_submit_button().click()

    """
    以下操作用于验证操作结果是否正确
    """

    # 取数据oid列内容
    def get_table_oid(self):
        return self.video_news_control_page.find_table_oid().text

    # 取数据操作列按钮内容
    def get_table_delivery_button_status(self):
        return self.video_news_control_page.find_table_delivery_button().text


# 视频监控页场景
class VideoNewsControlScenarios(object):
    def __init__(self, driver):
        self.video_news_control_oper = VideoNewsControlOper(driver)

    # 投放数据
    def delivery_video(self, oid, put_time):
        self.video_news_control_oper.input_oid(oid)
        self.video_news_control_oper.click_search_button()
        sleep(1)
        self.video_news_control_oper.click_delivery_button()
        sleep(1)
        self.video_news_control_oper.input_put_time(put_time)
        self.video_news_control_oper.click_submit_button()
