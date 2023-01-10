# -*- utf-8 -*-
# @Create Data: 2022/8/23 14:28
# @Author: guangyang219579
# @File: hot_24_feed_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from time import sleep


# 24小时feed版本页对象
class Hot24FeedPage(object):
    def __init__(self, driver):
        self.driver = driver

    """
    以下为24小时feed版本页面中的元素
    """

    # id元素(用于拼链接)
    def find_id_attribute(self, content):
        path = '//tr[contains(.,"' + str(content) + '")]'
        ele = self.driver.find_element(By.XPATH, path)
        return ele

    # 搜索框"消息ID"元素
    def find_content_id_input(self):
        ele = self.driver.find_element(By.NAME, 'commentId')
        return ele

    # 搜索框"状态"元素
    def find_status_select(self):
        ele = self.driver.find_element(By.ID, 'status')
        return ele

    # 搜索框"消息类型"元素
    def find_feedtype_select(self):
        ele = self.driver.find_element(By.ID, 'feedType')
        return ele

    # 搜索框"操作人"元素
    def find_operator_input(self):
        ele = self.driver.find_element(By.NAME, 'operator')
        return ele

    # "搜索按钮"元素
    def find_search_data_button(self):
        ele = self.driver.find_element(By.ID, 'searchData')
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    """
    以下为点击[创建新消息]按钮后弹窗中"信息"卡片中的元素，默认进入"纯文字"页面
    """

    # "消息正文输入框"元素
    def find_content_input(self):
        ele = self.driver.find_element(By.ID, 'contentEditor')
        return ele

    # "状态 - 撤回"元素
    def find_recall_label(self):
        ele = self.driver.find_element(By.XPATH, '//label[contains(.,"撤回")]')
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "保存按钮"元素
    def find_submit_button(self):
        ele = self.driver.find_element(By.XPATH, '//button[contains(.,"保存")]')
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "重要 - 是"元素
    def find_important_label(self):
        ele = self.driver.find_element(By.XPATH, '//label[contains(.,"重要")]/../div/label[contains(.,"是")]')
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "添加图片输入框"元素
    def find_pic_input(self):
        ele = self.driver.find_element(By.ID, 'addPic')
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "oid输入框"元素
    def find_oid_input(self):
        ele = self.driver.find_element(By.ID, 'oid')
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "裁剪按钮"元素
    def find_cut_pic_button(self):
        ele = self.driver.find_element(By.XPATH, '//input[@id="cutPic"]')
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "文字+外链"中"重要 - 是"元素
    def find_link_important_label(self):
        ele = self.driver.find_element(By.XPATH, '//label[contains(.,"重要")]/../label[contains(.,"是")]')
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele










    # "外链标题输入框"元素
    def find_link_title_input(self):
        ele = self.driver.find_element(By.ID, 'LinkTitle')
        return ele

    # "外链接地址输入框"元素
    def find_link_input(self):
        ele = self.driver.find_element(By.ID, 'link')
        return ele

    # "协议地址输入框"元素
    def find_agreement_input(self):
        ele = self.driver.find_element(By.ID, 'agreement')
        return ele

    """
    以下为列表数据元素
    """

    # "消息ID"元素
    def find_table_content_id(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[1]')
        return ele

    # "消息类型"元素
    def find_table_content_type(self, content_id):
        path = '//td[contains(.,"' + str(content_id) + '")]/../td[4]'
        ele = self.driver.find_element(By.XPATH, path)
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "消息正文"元素
    def find_table_content(self, content_id):
        path = '//td[contains(.,"' + str(content_id) + '")]/../td[6]/div'
        ele = self.driver.find_element(By.XPATH, path)
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "状态"元素
    def find_table_status(self, content_id):
        path = '//td[contains(.,"' + str(content_id) + '")]/../td[19]'
        ele = self.driver.find_element(By.XPATH, path)
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "重要"元素
    def find_table_important(self, content_id):
        path = '//td[contains(.,"' + str(content_id) + '")]/../td[12]'
        ele = self.driver.find_element(By.XPATH, path)
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "外链接标题"元素
    def find_table_link_title(self, content_id):
        path = '//td[contains(.,"' + str(content_id) + '")]/../td[7]'
        ele = self.driver.find_element(By.XPATH, path)
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "删除按钮"元素
    def find_table_delete_button(self, content_id):
        path = '//td[contains(.,"' + str(content_id) + '")]/../td[20]/a[3]'
        ele = self.driver.find_element(By.XPATH, path)
        js = "arguments[0].scrollTo(document.body.scrollWidth,0);"
        self.driver.execute_script(js, ele)
        return ele

    # "弹窗[确定]按钮"元素
    def find_accept_button(self):
        ele = self.driver.find_element(By.XPATH, '//div[contains(.,"确定要")]/div/a[1]')
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele


# 24小时feed页操作
class Hot24FeedOper(object):
    def __init__(self, driver):
        self.hot_24_feed_page = Hot24FeedPage(driver)
        self.wait = WebDriverWait(driver, 100)

    """
    以下操作用于场景中，模拟用户操作
    """

    # 输入消息ID
    def input_content_id(self, content_id):
        self.hot_24_feed_page.find_content_id_input().clear()
        self.hot_24_feed_page.find_content_id_input().send_keys(content_id)

    # 选择状态
    # 常用状态：{"发布": 0, "撤回": 1}
    def select_status(self, status_value):
        Select(self.hot_24_feed_page.find_status_select()).select_by_value(status_value)

    # 选择消息类型
    # 常用消息类型：{"纯文字": 1, "文字+图片": 2, "文字+视频": 3, "文字+外链": 4, "搜狐视频直播呼起": 5, "真人播报": 6}
    def select_feedtype(self, feed_type):
        Select(self.hot_24_feed_page.find_feedtype_select()).select_by_value(feed_type)

    # 输入操作人
    def input_operator(self, operator):
        self.hot_24_feed_page.find_operator_input().clear()
        self.hot_24_feed_page.find_operator_input().send_keys(operator)

    # 点击[搜索]按钮
    def click_search_data_button(self):
        self.hot_24_feed_page.driver.execute_script("arguments[0].click();",
                                                    self.hot_24_feed_page.find_search_data_button())

    # 输入消息正文
    def input_content(self, content):
        self.hot_24_feed_page.find_content_input().clear()
        self.hot_24_feed_page.find_content_input().send_keys(content)

    # 点击[状态 - 撤回]选项
    def click_recall_label(self):
        self.hot_24_feed_page.find_recall_label().click()

    # 点击[保存]按钮
    def click_submit_button(self):
        self.hot_24_feed_page.find_submit_button().click()

    # 点击[重要 - 是]选项
    def click_important_label(self):
        self.hot_24_feed_page.find_important_label().click()

    # 输入添加图片
    def input_pic(self, pic):
        self.hot_24_feed_page.find_pic_input().clear()
        self.hot_24_feed_page.find_pic_input().send_keys(pic)

    # 输入oid
    def input_oid(self, oid):
        self.hot_24_feed_page.find_oid_input().clear()
        self.hot_24_feed_page.find_oid_input().send_keys(oid)

    # 点击[裁剪]按钮
    def click_cut_pic_button(self):
        self.hot_24_feed_page.find_cut_pic_button().click()

    # 点击"文字+外链"中[重要 - 是]选项
    def click_link_important_label(self):
        self.hot_24_feed_page.find_link_important_label().click()









    # 输入外链标题
    def input_link_title(self, link_title):
        self.hot_24_feed_page.find_link_title_input().clear()
        self.hot_24_feed_page.find_link_title_input().send_keys(link_title)

    # 输入外链接地址
    def input_link(self, link):
        self.hot_24_feed_page.find_link_input().clear()
        self.hot_24_feed_page.find_link_input().send_keys(link)

    # 点击协议地址自动获取
    def click_agreement(self):
        self.hot_24_feed_page.driver.execute_script("arguments[0].click();",
                                                    self.hot_24_feed_page.find_agreement_input())









    # 点击[删除]按钮
    def click_table_delete_button(self, content_id):
        self.hot_24_feed_page.find_table_delete_button(content_id).click()

    # 点击弹窗[确定]按钮
    def click_accept_button(self):
        self.hot_24_feed_page.find_accept_button().click()

    """
    以下操作用于验证操作结果是否正确
    """

    # 取消息ID列内容
    def get_table_content_id(self):
        return self.hot_24_feed_page.find_table_content_id().text

    # 取消息类型列内容
    def get_table_content_type(self, content_id):
        return self.hot_24_feed_page.find_table_content_type(content_id).text

    # 取消息正文列内容
    def get_table_content(self, content_id):
        return self.hot_24_feed_page.find_table_content(content_id).text

    # 取消息正文列内容
    def get_table_status(self, content_id):
        return self.hot_24_feed_page.find_table_status(content_id).text

    # 取消息正文列内容
    def get_table_important(self, content_id):
        return self.hot_24_feed_page.find_table_important(content_id).text

    # 取外链接标题列内容
    def get_table_link_title(self, content_id):
        return self.hot_24_feed_page.find_table_link_title(content_id).text

    # 输出id属性
    def get_id_attribute(self, content):
        return self.hot_24_feed_page.find_id_attribute(content).get_attribute('id')


# 24小时feed页场景
class Hot24FeedScenarios(object):
    def __init__(self, driver):
        self.hot_24_feed_oper = Hot24FeedOper(driver)

    # 增加一条新纯文字数据
    def add_textli(self, content):
        self.hot_24_feed_oper.input_content(content)
        self.hot_24_feed_oper.click_recall_label()
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()

    # 编辑数据
    def edit_data(self):
        self.hot_24_feed_oper.click_important_label()
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()

    # 删除数据
    def delete_data(self, content_id):
        self.hot_24_feed_oper.click_table_delete_button(content_id)
        self.hot_24_feed_oper.click_accept_button()

    # 增加一条新文字+图片数据
    def add_picli(self, content, pic):
        self.hot_24_feed_oper.input_content(content)
        self.hot_24_feed_oper.input_pic(pic)
        self.hot_24_feed_oper.click_recall_label()
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()

    # 增加一条新文字+视频数据
    def add_videoli(self, content, oid):
        self.hot_24_feed_oper.input_oid(oid)
        self.hot_24_feed_oper.input_content(content)
        self.hot_24_feed_oper.click_recall_label()
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()

    # 增加一条新文字+外链数据
    def add_linkli(self, content, oid):
        self.hot_24_feed_oper.input_oid(oid)
        self.hot_24_feed_oper.input_content(content)
        self.hot_24_feed_oper.click_cut_pic_button()
        self.hot_24_feed_oper.click_recall_label()
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()

    # 编辑文字+外链数据
    def edit_link_data(self):
        self.hot_24_feed_oper.click_link_important_label()
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()







    # 增加一条新真人播报数据
    def add_listenli(self, oid, content, view_time):
        self.hot_24_feed_oper.input_oid(oid)
        self.hot_24_feed_oper.input_content(content)
        self.hot_24_feed_oper.click_mark_mode_recommend()
        self.hot_24_feed_oper.input_view_time(view_time)
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()

    # 查询新建数据(首次查询，为得出content_id)
    def search_new_data(self, status, feedtype):
        self.hot_24_feed_oper.select_status(status)
        self.hot_24_feed_oper.select_feedtype(feedtype)
        self.hot_24_feed_oper.input_operator("guangyang")
        sleep(3)
        self.hot_24_feed_oper.click_search_data_button()
        sleep(3)

    # 查询数据
    def search_data(self, content_id):
        self.hot_24_feed_oper.input_content_id(content_id)
        self.hot_24_feed_oper.click_search_data_button()
