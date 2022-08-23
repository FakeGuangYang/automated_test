# -*- utf-8 -*-
# @Create Data: 2022/8/23 14:28
# @Author: guangyang219579
# @File: hot_24_feed_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from Common.parse_csv import parse_csv
from time import sleep
from deprecated.sphinx import deprecated


# 24小时feed页对象
class Hot24FeedPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.oid = parse_csv("Data/test_scheduled_pushing_news_add_modal.csv")[0][1]

    """
    以下为24小时feed页面中的元素
    """

    # 搜索框"操作人"元素
    def find_operator(self):
        ele = self.driver.find_element(By.NAME, 'operator')
        return ele

    # "搜索按钮"元素
    def find_search_data_button(self):
        ele = self.driver.find_element(By.ID, 'searchData')
        return ele

    # "创建新消息按钮"元素
    def find_add_content(self):
        ele = self.driver.find_element(By.ID, 'add')
        return ele

    """
    以下为点击[创建新消息]按钮后弹窗中"信息"卡片中的元素，默认进入"纯文字"页面
    """

    # "文字+图片tab"元素
    def find_picli_tab(self):
        ele = self.driver.find_element(By.ID, 'picli')
        return ele

    # "文字+视频tab"元素
    def find_videoli_tab(self):
        ele = self.driver.find_element(By.ID, 'videoli')
        return ele

    # "文字+外链tab"元素
    def find_linkli_tab(self):
        ele = self.driver.find_element(By.ID, 'linkli')
        return ele

    # "搜狐视频直播呼起tab"元素
    def find_sohuVideoli_tab(self):
        ele = self.driver.find_element(By.ID, 'sohuVideoli')
        return ele

    # "真人播报tab"元素
    def find_Listenli_tab(self):
        ele = self.driver.find_element(By.ID, 'Listenli')
        return ele

    # "消息正文输入框"元素
    def find_content_editor_input(self):
        ele = self.driver.find_element(By.ID, 'contentEditor')
        return ele

    # "显示时间输入框"元素
    def find_view_time_input(self):
        ele = self.driver.find_element(By.ID, 'viewTime')
        return ele

    # "添加图片输入框"元素
    def find_add_pic_input(self):
        ele = self.driver.find_element(By.ID, 'addPic')
        return ele

    # "oid输入框"元素
    def find_oid_input(self):
        ele = self.driver.find_element(By.ID, 'oid')
        return ele

    # "裁剪按钮"元素
    def find_cut_pic_button(self):
        ele = self.driver.find_element(By.ID, 'cutPic')
        return ele

    # "标题输入框"元素
    def find_link_title_input(self):
        ele = self.driver.find_element(By.ID, 'LinkTitle')
        return ele

    # "外链接地址输入框"元素
    def find_link_input(self):
        ele = self.driver.find_element(By.ID, 'link')
        return ele

    # "保存按钮"元素
    def find_submit_button(self):
        ele = self.driver.find_element(By.ID, 'submit')
        return ele

    """
    以下为列表数据元素
    """

    # "消息类型"元素
    def find_table_content_type(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[4]')
        return ele

    # "外链接标题"元素
    def find_table_oid(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[7]')
        return ele

    # "状态"元素
    def find_table_status(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[19]')
        return ele

    # "撤回/发布按钮"元素
    def find_table_recall_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[20]/a[1]')
        return ele

    # "编辑按钮"元素
    def find_table_edit_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[20]/a[2]')
        return ele

    # "删除按钮"元素
    def find_table_delete_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[20]/a[3]')
        return ele


# 定投管理页操作
class Hot24FeedOper(object):
    def __init__(self, driver):
        self.scheduled_pushing_page = Hot24FeedPage(driver)
        self.wait = WebDriverWait(driver, 100)

    """
    以下操作用于场景中，模拟用户操作
    """

    # 点击[添加]按钮
    def click_add_modal_button(self):
        self.scheduled_pushing_page.find_add_modal_button().click()

    # 点击"指定cid投放"选项
    # 下句由于页面未加载出元素导致报错，因此弃用
    # self.scheduled_pushing_page.find_cids_label().click()
    def click_cids_label(self):
        self.wait.until(
            expected_conditions.element_to_be_clickable(self.scheduled_pushing_page.find_cids_label())
        ).click()
