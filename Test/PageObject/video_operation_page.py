# -*- utf-8 -*-
# @Create Data: 2022/6/22 10:23
# @Author: guangyang219579
# @File: video_operation_page.py

from Common.parse_csv import parse_csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from time import sleep

sleep_time = 4


# 视频运营页对象
class VideoOperationPage(object):
    def __init__(self, driver):
        self.driver = driver

    """
    以下为视频运营页面中的元素
    """

    # "newsid搜索框"元素
    def find_search_newsid_input(self):
        ele = self.driver.find_element(By.ID, 'newsid')
        return ele

    # "搜索按钮"元素
    def find_search_content_button(self):
        ele = self.driver.find_element(By.ID, 'search_content')
        return ele

    # "添加按钮"元素
    def find_add_content_button(self):
        ele = self.driver.find_element(By.ID, 'add_content')
        return ele

    """
    以下为点击[添加]按钮后弹窗中"添加"卡片中的元素
    """

    # "newsid"元素
    def find_newsid_input(self):
        ele = self.driver.find_element(By.ID, 'newsid1')
        return ele

    # "账号昵称"元素
    def find_nickname_input(self):
        ele = self.driver.find_element(By.ID, 'nickname')
        return ele

    # "投放时间"元素
    def find_put_time_input(self):
        ele = self.driver.find_element(By.ID, 'put_time')
        return ele

    # "优先级"元素
    def find_priority_select(self):
        ele = self.driver.find_element(By.ID, 'priority_add')
        return ele

    # "标签词"元素
    def find_tag_input(self):
        ele = self.driver.find_element(By.ID, 'tag-input-put')
        return ele

    # "标签词的[添加]按钮"元素
    def find_add_tag_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="tag-input-put"]/../button')
        return ele

    # "确认按钮"元素
    def find_submit_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@class="modal-footer"]/button[1]')
        return ele

    # "取消按钮"元素
    def find_cancel_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@class="modal-footer"]/button[2]')
        return ele

    """
    以下为视频运营列表数据元素
    """

    # "数据列表newsid"元素
    def find_table_newsid(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="common_table"]/tbody/tr[1]/td[1]')
        return ele

    # "数据列表标题"元素
    def find_table_title(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="common_table"]/tbody/tr[1]/td[3]/a')
        return ele

    # "数据列表帐号昵称"元素
    def find_table_nickname(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="common_table"]/tbody/tr[1]/td[4]')
        return ele

    # "数据列表优先级"元素
    def find_table_priority(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="common_table"]/tbody/tr[1]/td[6]')
        return ele

    # "数据列表标签词"元素
    def find_table_tags(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="common_table"]/tbody/tr[1]/td[7]')
        return ele

    # "数据列表状态"元素
    def find_table_status(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="common_table"]/tbody/tr[1]/td[13]')
        return ele

    # "数据列表[移除]按钮"元素
    def find_table_remove_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="common_table"]/tbody/tr[1]/td[14]/div/button[1]')
        return ele

    # "数据列表[编辑]按钮"元素
    def find_table_edit_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="common_table"]/tbody/tr[1]/td[14]/div/button[2]')
        return ele

    # "数据列表未查询到数据缺省文案"元素
    def find_table_default_content(self):
        ele = self.driver.find_element(By.CLASS_NAME, 'dataTables_empty')
        return ele


# 视频运营页操作
class VideoOperationOper(object):
    def __init__(self, driver):
        self.video_operation_page = VideoOperationPage(driver)
        self.wait = WebDriverWait(driver, 100)

    """
    以下操作用于场景中，模拟用户操作
    """

    # 点击[添加]按钮
    def click_add_content_button(self):
        self.video_operation_page.find_add_content_button().click()

    # 输入newsid
    def input_newsid(self, newsid):
        self.video_operation_page.find_newsid_input().clear()
        self.video_operation_page.find_newsid_input().send_keys(newsid)

    # 输入帐号昵称
    def input_nickname(self, nickname):
        # 加click()为了在输入投放时间后能关闭选择时间控件
        self.video_operation_page.find_nickname_input().click()
        self.video_operation_page.find_nickname_input().clear()
        self.video_operation_page.find_nickname_input().send_keys(nickname)

    # 输入投放时间
    def input_put_time(self, put_time):
        self.video_operation_page.find_put_time_input().clear()
        self.video_operation_page.find_put_time_input().send_keys(put_time)

    # 选择优先级 {"普通": 1, "高时效": 2}
    def select_priority(self, priority_value):
        Select(self.video_operation_page.find_priority_select()).select_by_value(priority_value)

    # 输入标签词
    def input_tag(self, tag):
        # 加click()为了在输入投放时间后能关闭选择时间控件
        self.video_operation_page.find_nickname_input().click()
        self.video_operation_page.find_tag_input().clear()
        self.video_operation_page.find_tag_input().send_keys(tag)

    # 点击标签词[添加]按钮
    def click_add_tag_button(self):
        self.video_operation_page.find_add_tag_button().click()

    # 点击[确认]按钮
    def click_submit_button(self):
        self.video_operation_page.find_submit_button().click()

    # 搜索框输入newsid作为检索条件
    def input_search_newsid(self, newsid):
        self.video_operation_page.find_search_newsid_input().clear()
        self.video_operation_page.find_search_newsid_input().send_keys(newsid)

    # 点击[搜索]按钮
    def click_search_content_button(self):
        self.video_operation_page.find_search_content_button().click()

    # 点击[移除]按钮
    def click_remove_button(self):
        self.video_operation_page.find_table_remove_button().click()

    # 点击[编辑]按钮
    def click_edit_button(self):
        self.video_operation_page.find_table_edit_button().click()

    """
    以下操作用于验证操作结果是否正确
    """

    # 取数据newsid列内容
    def get_table_newsid(self):
        return self.video_operation_page.find_table_newsid().text

    # 取数据标题列内容
    def get_table_title(self):
        return self.video_operation_page.find_table_title().text

    # 取数据帐号昵称列内容
    def get_table_nickname(self):
        return self.video_operation_page.find_table_nickname().text

    # 取数据优先级列内容
    def get_table_priority(self):
        return self.video_operation_page.find_table_priority().text

    # 取数据标签词列内容
    def get_table_tags(self):
        return self.video_operation_page.find_table_tags().text

    # 取数据状态列内容
    def get_table_status(self):
        return self.video_operation_page.find_table_status().text

    # 取未查询到数据缺省文案内容
    def get_table_default_content(self):
        return self.video_operation_page.find_table_default_content().text


# 视频运营页场景
class VideoOperationScenarios(object):
    def __init__(self, driver):
        self.video_operation_oper = VideoOperationOper(driver)
        self.newsid = parse_csv("../../Data/test_video_operation_add_content.csv")[0][1]

    # 增加一条新数据
    def add_content(self, newsid, put_time, tag, priority_value):
        self.video_operation_oper.click_add_content_button()
        sleep(sleep_time)
        self.video_operation_oper.input_newsid(newsid)
        sleep(sleep_time)
        self.video_operation_oper.input_put_time(put_time)
        self.video_operation_oper.input_tag(tag)
        self.video_operation_oper.click_add_tag_button()
        self.video_operation_oper.select_priority(priority_value)
        self.video_operation_oper.click_submit_button()

    # 编辑新添加的数据
    def edit_content(self, new_tag):
        self.video_operation_oper.input_search_newsid(self.newsid)
        self.video_operation_oper.click_search_content_button()
        sleep(sleep_time)
        self.video_operation_oper.click_edit_button()
        sleep(sleep_time)
        self.video_operation_oper.input_tag(new_tag)
        self.video_operation_oper.click_add_tag_button()
        self.video_operation_oper.click_submit_button()

    # 移除新添加的数据
    def remove_content(self):
        self.video_operation_oper.input_search_newsid(self.newsid)
        self.video_operation_oper.click_search_content_button()
        sleep(sleep_time)
        self.video_operation_oper.click_remove_button()
