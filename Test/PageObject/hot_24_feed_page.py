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
    def find_id_attribute(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr')
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
        return ele

    # "创建新消息按钮"元素
    def find_add_content_button(self):
        ele = self.driver.find_element(By.ID, 'add')
        return ele

    """
    以下为点击[创建新消息]按钮后弹窗中"信息"卡片中的元素，默认进入"纯文字"页面
    """

    # "文字+图片tab"元素
    # 由于页面是用iframe嵌套的，故没有使用此元素
    def find_picli_tab(self):
        ele = self.driver.find_element(By.ID, 'picli')
        return ele

    # "文字+视频tab"元素
    # 由于页面是用iframe嵌套的，故没有使用此元素
    def find_videoli_tab(self):
        ele = self.driver.find_element(By.ID, 'videoli')
        return ele

    # "文字+外链tab"元素
    # 由于页面是用iframe嵌套的，故没有使用此元素
    def find_linkli_tab(self):
        ele = self.driver.find_element(By.ID, 'linkli')
        return ele

    # "搜狐视频直播呼起tab"元素
    # 由于页面是用iframe嵌套的，故没有使用此元素
    def find_sohuvideoli_tab(self):
        ele = self.driver.find_element(By.ID, 'sohuVideoli')
        return ele

    # "真人播报tab"元素
    # 由于页面是用iframe嵌套的，故没有使用此元素
    def find_listenli_tab(self):
        ele = self.driver.find_element(By.ID, 'Listenli')
        return ele

    # "消息正文输入框"元素
    def find_content_input(self):
        ele = self.driver.find_element(By.ID, 'contentEditor')
        return ele

    # "显示时间输入框"元素
    def find_view_time_input(self):
        ele = self.driver.find_element(By.ID, 'viewTime')
        return ele

    # "显示时间输入框确定按钮"元素
    def find_view_time_submit_button(self):
        ele = self.driver.find_element(By.ID, 'dpOkInput')
        return ele

    # "高亮标识 - 无"元素
    def find_mark_mode_none(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="mark_0"]/../label[1]')
        return ele

    # "高亮标识 - 推荐"元素
    def find_mark_mode_recommend(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="mark_0"]/../label[5]')
        return ele

    # 搜狐视频直播呼起"高亮标识 - 推荐"元素
    def find_sohuvideo_mark_mode_recommend(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="mark_0"]/../label[6]')
        return ele

    # "重要 - 否"元素
    def find_is_important_no(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="isImportant_0"]/../label[1]')
        return ele

    # 文字+外链"重要 - 否"元素
    def find_link_is_important_no(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="isImportant_0"]/../label[2]')
        return ele

    # "添加图片输入框"元素
    def find_pic_input(self):
        ele = self.driver.find_element(By.ID, 'addPic')
        return ele

    # "搜狐视频直播呼起添加图片输入框"元素
    def find_sohuvideo_pic_input(self):
        ele = self.driver.find_element(By.ID, 'picLoad')
        return ele

    # "oid输入框"元素
    def find_oid_input(self):
        ele = self.driver.find_element(By.ID, 'oid')
        return ele

    # "裁剪按钮"元素
    def find_cut_pic_button(self):
        ele = self.driver.find_element(By.ID, 'cutPic')
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

    # "保存按钮"元素
    def find_submit_button(self):
        ele = self.driver.find_element(By.ID, 'save')
        return ele

    # 文字+图片"保存按钮"元素(与其他页面不一致)
    def find_pic_submit_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="close"]/../button[1]')
        return ele

    """
    以下为列表数据元素
    """

    # "消息ID"元素
    def find_table_content_id(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[1]')
        return ele

    # "消息类型"元素
    def find_table_content_type(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[4]')
        return ele

    # "消息正文"元素
    def find_table_content(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[6]/div')
        return ele

    # "外链接标题"元素
    def find_table_link_title(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[7]')
        return ele

    # "重要"元素
    def find_table_important(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="dataTable"]/tbody/tr[1]/td[12]')
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

    # "弹窗[确定]按钮"元素
    def find_accept_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@class="layui-layer layui-layer-dialog"]/div[3]/a[1]')
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
        self.hot_24_feed_page.find_search_data_button().click()

    # 点击[创建新消息]按钮
    def click_add_content_button(self):
        self.hot_24_feed_page.find_add_content_button().click()

    # 点击[文字+图片]tab
    # 由于页面是用iframe嵌套的，故没有使用此操作
    def click_picli_tab(self):
        self.hot_24_feed_page.find_picli_tab().click()

    # 点击[文字+视频]tab
    # 由于页面是用iframe嵌套的，故没有使用此操作
    def click_videoli_tab(self):
        self.hot_24_feed_page.find_videoli_tab().click()

    # 点击[文字+外链]tab
    # 由于页面是用iframe嵌套的，故没有使用此操作
    def click_linkli_tab(self):
        self.hot_24_feed_page.find_linkli_tab().click()

    # 点击[搜狐视频直播呼起]tab
    # 由于页面是用iframe嵌套的，故没有使用此操作
    def click_sohuvideoli_tab(self):
        self.hot_24_feed_page.find_sohuvideoli_tab().click()

    # 点击[真人播报]tab
    # 由于页面是用iframe嵌套的，故没有使用此操作
    def click_listenli_tab(self):
        self.hot_24_feed_page.find_listenli_tab().click()

    # 输入消息正文
    def input_content(self, content):
        self.hot_24_feed_page.find_content_input().clear()
        self.hot_24_feed_page.find_content_input().send_keys(content)

    # 输入显示时间
    def input_view_time(self, view_time):
        self.hot_24_feed_page.find_view_time_input().clear()
        self.hot_24_feed_page.find_view_time_input().send_keys(view_time)

    # 输入显示时间
    def click_view_time_submit_button(self):
        self.hot_24_feed_page.find_view_time_submit_button().click()

    # 点击[高亮标识 - 无]选项
    def click_mark_mode_none(self):
        self.hot_24_feed_page.find_mark_mode_none().click()

    # 点击[高亮标识 - 推荐]选项
    def click_mark_mode_recommend(self):
        self.hot_24_feed_page.find_mark_mode_recommend().click()

    # 点击搜狐视频直播呼起[高亮标识 - 推荐]选项
    def click_sohuvideo_mark_mode_recommend(self):
        self.hot_24_feed_page.find_sohuvideo_mark_mode_recommend().click()

    # 点击[重要 - 否]选项
    def click_is_important_no(self):
        self.hot_24_feed_page.find_is_important_no().click()

    # 点击文字+外链[重要 - 否]选项
    def click_link_is_important_no(self):
        self.hot_24_feed_page.find_link_is_important_no().click()

    # 输入添加图片
    def input_pic(self, pic):
        self.hot_24_feed_page.find_pic_input().clear()
        self.hot_24_feed_page.find_pic_input().send_keys(pic)

    # 输入搜狐视频直播呼起添加图片
    def input_sohuvideo_pic(self, pic):
        self.hot_24_feed_page.find_sohuvideo_pic_input().clear()
        self.hot_24_feed_page.find_sohuvideo_pic_input().send_keys(pic)

    # 输入oid
    def input_oid(self, oid):
        self.hot_24_feed_page.find_oid_input().clear()
        self.hot_24_feed_page.find_oid_input().send_keys(oid)

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
        self.hot_24_feed_page.find_agreement_input().click()

    # 点击[裁剪]按钮
    def click_cut_pic_button(self):
        self.hot_24_feed_page.find_cut_pic_button().click()

    # 点击[保存]按钮
    def click_submit_button(self):
        self.hot_24_feed_page.find_submit_button().click()

    # 点击文字+图片[保存]按钮
    def click_pic_submit_button(self):
        self.hot_24_feed_page.find_pic_submit_button().click()

    # 点击[撤回/发布]按钮
    def click_table_recall_button(self):
        self.hot_24_feed_page.find_table_recall_button().click()

    # 点击[编辑]按钮
    def click_table_edit_button(self):
        self.hot_24_feed_page.find_table_edit_button().click()

    # 点击[删除]按钮
    def click_table_delete_button(self):
        self.hot_24_feed_page.find_table_delete_button().click()

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
    def get_table_content_type(self):
        return self.hot_24_feed_page.find_table_content_type().text

    # 取消息正文列内容
    def get_table_content(self):
        return self.hot_24_feed_page.find_table_content().text

    # 取外链接标题列内容
    def get_table_link_title(self):
        return self.hot_24_feed_page.find_table_link_title().text

    # 取状态列内容
    def get_table_status(self):
        return self.hot_24_feed_page.find_table_status().text

    # 取重要列内容
    def get_table_important(self):
        return self.hot_24_feed_page.find_table_important().text

    # 输出id属性
    def get_id_attribute(self):
        return self.hot_24_feed_page.find_id_attribute().get_attribute('id')


# 24小时feed页场景
class Hot24FeedScenarios(object):
    def __init__(self, driver):
        self.hot_24_feed_oper = Hot24FeedOper(driver)

    # 增加一条新纯文字数据
    def add_textli(self, content, view_time):
        self.hot_24_feed_oper.input_content(content)
        self.hot_24_feed_oper.click_mark_mode_recommend()
        self.hot_24_feed_oper.input_view_time(view_time)
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()

    # 增加一条新文字+图片数据
    def add_picli(self, content, pic, view_time):
        self.hot_24_feed_oper.input_content(content)
        self.hot_24_feed_oper.click_mark_mode_recommend()
        self.hot_24_feed_oper.input_pic(pic)
        self.hot_24_feed_oper.input_view_time(view_time)
        sleep(2)
        self.hot_24_feed_oper.click_pic_submit_button()

    # 编辑文字+图片数据
    def edit_pic_data(self):
        self.hot_24_feed_oper.click_is_important_no()
        sleep(2)
        self.hot_24_feed_oper.click_pic_submit_button()

    # 增加一条新文字+视频数据
    def add_videoli(self, content, oid, view_time):
        self.hot_24_feed_oper.input_oid(oid)
        self.hot_24_feed_oper.input_content(content)
        self.hot_24_feed_oper.click_mark_mode_recommend()
        self.hot_24_feed_oper.input_view_time(view_time)
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()

    # 增加一条新文字+外链数据
    def add_linkli(self, content, oid, view_time):
        self.hot_24_feed_oper.input_oid(oid)
        self.hot_24_feed_oper.input_content(content)
        sleep(2)
        self.hot_24_feed_oper.click_cut_pic_button()
        self.hot_24_feed_oper.click_mark_mode_recommend()
        sleep(3)
        self.hot_24_feed_oper.input_view_time(view_time)
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()

    # 编辑文字+外链数据
    def edit_link_data(self):
        self.hot_24_feed_oper.click_link_is_important_no()
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()

    # 增加一条新搜狐视频直播呼起数据
    def add_sohuvideoli(self, link_title, link, content, pic, view_time):
        self.hot_24_feed_oper.input_link_title(link_title)
        self.hot_24_feed_oper.input_link(link)
        self.hot_24_feed_oper.click_agreement()
        self.hot_24_feed_oper.input_sohuvideo_pic(pic)
        self.hot_24_feed_oper.input_content(content)
        sleep(2)
        self.hot_24_feed_oper.click_cut_pic_button()
        self.hot_24_feed_oper.click_sohuvideo_mark_mode_recommend()
        sleep(2)
        self.hot_24_feed_oper.input_view_time(view_time)
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()

    # 编辑搜狐视频直播呼起数据
    def edit_sohuvideo_data(self):
        self.hot_24_feed_oper.click_link_is_important_no()
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

    # 编辑数据
    def edit_data(self):
        self.hot_24_feed_oper.click_is_important_no()
        sleep(2)
        self.hot_24_feed_oper.click_submit_button()

    # 撤回数据
    def recall_data(self):
        self.hot_24_feed_oper.click_table_recall_button()
        self.hot_24_feed_oper.click_accept_button()

    # 删除数据
    def delete_data(self):
        self.hot_24_feed_oper.click_table_delete_button()
        self.hot_24_feed_oper.click_accept_button()

    # 查询新建数据(首次查询，为得出content_id)
    def search_new_data(self, status, feedtype):
        self.hot_24_feed_oper.select_status(status)
        self.hot_24_feed_oper.select_feedtype(feedtype)
        self.hot_24_feed_oper.input_operator("guangyang")
        self.hot_24_feed_oper.click_search_data_button()
        return

    # 查询数据
    def search_data(self, content_id):
        self.hot_24_feed_oper.input_content_id(content_id)
        self.hot_24_feed_oper.click_search_data_button()
