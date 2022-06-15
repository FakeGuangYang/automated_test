# -*- utf-8 -*-
# @Create Data: 2022/6/9 09:22
# @Author: guangyang219579
# @File: scheduled_pushing_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from Common.parse_csv import parse_csv
from time import sleep


# 定投管理页对象
class ScheduledPushing(object):
    def __init__(self, driver):
        self.driver = driver
        self.oid = parse_csv("../../Data/test_news_add_modal.csv")[0][1]

    """
    以下为定投管理页面中的元素
    """

    # 搜索框"投放id"元素
    def find_oid(self):
        ele = self.driver.find_element(By.ID, 'oid')
        return ele

    # 搜索框"标题"元素
    def find_title(self):
        ele = self.driver.find_element(By.ID, 'title')
        return ele

    # 搜索框"操作人"元素
    def find_operator(self):
        ele = self.driver.find_element(By.ID, 'operator')
        return ele

    # 搜索框"备注"元素
    def find_remark_search(self):
        ele = self.driver.find_element(By.ID, 'remark_search')
        return ele

    # "一刷条数控制按钮"元素
    def find_num_control_button(self):
        ele = self.driver.find_element(By.ID, 'num_control')
        return ele

    # "搜索按钮"元素
    def find_search_content_button(self):
        ele = self.driver.find_element(By.ID, 'search_content')
        return ele

    # "添加按钮"元素
    def find_add_modal_button(self):
        ele = self.driver.find_element(By.ID, 'add_modal')
        return ele

    """
    以下为点击[添加]按钮后弹窗中"投放人群"卡片中的元素
    """

    # "目标人群-线上投放"元素
    def find_living_label(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="realLiving"]/../label[1]')
        return ele

    # "目标人群-指定cid投放"元素
    def find_cids_label(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="realCids"]/../label[2]')
        return ele

    # "cids输入框"元素
    def find_cids_input(self):
        ele = self.driver.find_element(By.ID, 'cids')
        return ele

    # "目标人群-指定分桶"元素
    def find_buckets_label(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="realBuckets"]/../label[3]')
        return ele

    """
    以下为点击[添加]按钮后弹窗中"投放内容"卡片中的元素
    """

    # "投放id输入框"元素
    def find_new_oid_input(self):
        ele = self.driver.find_element(By.ID, 'new_oid')
        return ele

    # "投放时间输入框"元素
    def find_delivery_time(self):
        ele = self.driver.find_element(By.ID, 'delivery_time')
        return ele

    # "开始时间小时"元素
    def find_start_hour_input(self):
        ele = self.driver.find_element(By.XPATH,
                                       '//*[@class="calendar left"]/*[@class="daterangepicker_input"]/'
                                       '*[@class="calendar-time"]/div/*[@class="hourselect"]')
        return ele

    # "开始时间分钟"元素
    def find_start_minute_input(self):
        ele = self.driver.find_element(By.XPATH,
                                       '//*[@class="calendar left"]/*[@class="daterangepicker_input"]/'
                                       '*[@class="calendar-time"]/div/*[@class="minuteselect"]')
        return ele

    # "结束时间小时"元素
    def find_end_hour_input(self):
        ele = self.driver.find_element(By.XPATH,
                                       '//*[@class="calendar right"]/*[@class="daterangepicker_input"]/'
                                       '*[@class="calendar-time"]/div/*[@class="hourselect"]')
        return ele

    # "结束时间分钟"元素
    def find_end_minute_input(self):
        ele = self.driver.find_element(By.XPATH,
                                       '//*[@class="calendar right"]/*[@class="daterangepicker_input"]/'
                                       '*[@class="calendar-time"]/div/*[@class="minuteselect"]')
        return ele

    # "确认按钮"元素
    def find_apply_button_in_delivery_time(self):
        ele = self.driver.find_element(By.XPATH, '//*[@class="range_inputs"]/button[1]')
        return ele

    # "取消按钮"元素
    def find_cancel_button_in_delivery_time(self):
        ele = self.driver.find_element(By.CLASS_NAME, 'cancelBtn btn btn-sm btn-default')
        return ele

    # "取消按钮"元素
    def find_feed_uid_input(self):
        ele = self.driver.find_element(By.ID, 'changeUid1')
        return ele

    """
    以下为点击[添加]按钮后弹窗中"投放位置"卡片中的元素
    """

    # 线上投放/指定cid投放"投放频道"元素
    def find_channel(self):
        ele = self.driver.find_element(By.NAME, 'channel')
        return ele

    # 指定分桶"投放频道"元素
    def find_bucket_channel(self):
        ele = self.driver.find_element(By.NAME, 'bucketChannel')
        return ele

    # "流内位置"元素
    def find_location(self):
        ele = self.driver.find_element(By.ID, 'location')
        return ele

    """
    以下为点击[添加]按钮后弹窗中"其他控制项"卡片中的元素
    """

    # "是否一刷仍然出现"元素
    def find_one_flash_fade(self):
        ele = self.driver.find_element(By.ID, 'one_flash_fade')
        return ele

    # "曝光顺序权重输入框"元素
    def find_weight_input(self):
        ele = self.driver.find_element(By.ID, 'weight')
        return ele

    # "备注输入框"元素
    def find_remark_input(self):
        ele = self.driver.find_element(By.ID, 'remark')
        return ele

    """
    以下为点击[添加]按钮后弹窗中的[保存]/[取消]按钮元素
    """

    # "保存按钮"元素
    def find_save_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="content_body"]/form/button[1]')
        return ele

    # "取消按钮"元素
    def find_cancel_button_in_add_modal(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="content_body"]/form/button[2]')
        return ele

    """
    以下为新闻定投列表数据元素
    """

    # "数据内容类型"元素
    def find_table_content_type(self):
        ele = self.driver.find_element(By.XPATH, '//*[@oid=' + self.oid + '][1]/td[1]')
        return ele

    # "数据投放id"元素
    def find_table_oid(self):
        ele = self.driver.find_element(By.XPATH, '//*[@oid=' + self.oid + '][1]/td[2]')
        return ele

    # "数据标题"元素
    def find_table_title(self):
        ele = self.driver.find_element(By.XPATH, '//*[@oid=' + self.oid + '][1]/td[3]')
        return ele

    # "数据投放位置"元素
    def find_table_delivery_position(self):
        ele = self.driver.find_element(By.XPATH, '//*[@oid=' + self.oid + '][1]/td[7]')
        return ele

    # "数据备注"元素
    def find_table_remark(self):
        ele = self.driver.find_element(By.XPATH, '//*[@oid=' + self.oid + '][1]/td[8]')
        return ele

    # "数据状态"元素
    def find_table_status(self):
        ele = self.driver.find_element(By.XPATH, '//*[@oid=' + self.oid + '][1]/td[9]')
        return ele

    # "投放/取消投放按钮"元素
    def find_table_delivery_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@oid=' + self.oid + '][1]/td[11]/div/button[1]')
        return ele

    # "编辑按钮"元素
    def find_table_edit_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@oid=' + self.oid + '][1]/td[11]/div/button[2]')
        return ele

    # "成功"弹窗
    def find_success_toast(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="layui-layer4"]/div')
        return ele

    """
    以下为音频定投列表数据元素
    """

    # "投放uid"元素
    def find_feed_uid(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="list_table"]/tbody/tr[1]/td[1]')
        return ele

    # "音频标题"元素
    def find_audio_title(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="list_table"]/tbody/tr[1]/td[2]')
        return ele

    # "投放位置"元素
    def find_audio_delivery_position(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="list_table"]/tbody/tr[1]/td[6]')
        return ele

    # "备注"元素
    def find_audio_remark(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="list_table"]/tbody/tr[1]/td[7]')
        return ele

    # "投放位置"元素
    def find_audio_status(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="list_table"]/tbody/tr[1]/td[8]')
        return ele

    # "投放/取消投放按钮"元素
    def find_audio_delivery_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="list_table"]/tbody/tr[1]/td[10]/div/button[1]')
        return ele

    # "编辑按钮"元素
    def find_audio_edit_button(self):
        ele = self.driver.find_element(By.XPATH, '//*[@id="list_table"]/tbody/tr[1]/td[10]/div/button[2]')
        return ele


# 定投管理页操作
class ScheduledPushingOper(object):
    def __init__(self, driver):
        self.scheduled_pushing_page = ScheduledPushing(driver)
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

    # 在cids输入框输入cid
    def input_cids(self, cids):
        self.scheduled_pushing_page.find_cids_input().clear()
        self.scheduled_pushing_page.find_cids_input().send_keys(cids)

    # 输入投放id
    # 由于界面限制，不能输入只能粘贴，因此弃用本方法
    # self.scheduled_pushing_page.find_new_oid_input().clear()
    # self.scheduled_pushing_page.find_new_oid_input().send_keys(oid)
    def input_new_oid(self, oid):
        self.scheduled_pushing_page.find_cids_input().clear()
        self.scheduled_pushing_page.find_cids_input().send_keys(oid)
        self.scheduled_pushing_page.find_cids_input().send_keys(Keys.CONTROL, 'a')
        self.scheduled_pushing_page.find_cids_input().send_keys(Keys.CONTROL, 'x')
        self.scheduled_pushing_page.find_new_oid_input().clear()
        self.scheduled_pushing_page.find_new_oid_input().send_keys(Keys.CONTROL, 'v')

    # 输入投放feed_uid
    def input_new_uid(self, uid):
        self.scheduled_pushing_page.find_cids_input().clear()
        self.scheduled_pushing_page.find_cids_input().send_keys(uid)
        self.scheduled_pushing_page.find_cids_input().send_keys(Keys.CONTROL, 'a')
        self.scheduled_pushing_page.find_cids_input().send_keys(Keys.CONTROL, 'x')
        self.scheduled_pushing_page.find_feed_uid_input().clear()
        self.scheduled_pushing_page.find_feed_uid_input().send_keys(Keys.CONTROL, 'v')

    # 选择投放频道
    # 常用投放频道：{"首页": 1, "推荐": 13557}
    def select_channel(self, channel_value):
        Select(self.scheduled_pushing_page.find_channel()).select_by_value(channel_value)

    # 输入流内位置
    def input_location(self, location):
        self.scheduled_pushing_page.find_location().clear()
        self.scheduled_pushing_page.find_location().send_keys(location)

    # 输入曝光顺序权重
    def input_weight(self, weight):
        self.scheduled_pushing_page.find_weight_input().clear()
        self.scheduled_pushing_page.find_weight_input().send_keys(weight)

    # 输入备注
    def input_remark(self, remark):
        self.scheduled_pushing_page.find_remark_input().clear()
        # 为了编辑的时候清除备注后能再次输入新备注，因此设置2s的停顿
        sleep(3)
        self.scheduled_pushing_page.find_remark_input().send_keys(remark)

    # 点击投放时间，打开日历
    def click_delivery_time(self):
        self.scheduled_pushing_page.find_delivery_time().click()

    # 输入结束小时
    def input_end_time_hour(self):
        hour = Select(self.scheduled_pushing_page.find_start_hour_input()).first_selected_option.text
        Select(self.scheduled_pushing_page.find_end_hour_input()).select_by_value(hour)

    # 输入结束分钟
    def input_end_time_minute(self):
        minute = Select(self.scheduled_pushing_page.find_start_minute_input()).first_selected_option.text
        minute = str(int(minute) + 3)
        Select(self.scheduled_pushing_page.find_end_minute_input()).select_by_value(minute)

    # 点击保存按钮
    def click_save_button(self):
        self.scheduled_pushing_page.find_save_button().click()

    # 点击投放/取消投放按钮
    def click_table_delivery_button(self):
        return self.scheduled_pushing_page.find_table_delivery_button().click()

    # 点击编辑按钮
    def click_table_edit_button(self):
        return self.scheduled_pushing_page.find_table_edit_button().click()

    # 输入操作人
    def input_operator(self):
        self.scheduled_pushing_page.find_operator().send_keys("guangyang219579")

    # 点击搜索按钮
    def click_search_content_button(self):
        return self.scheduled_pushing_page.find_search_content_button().click()

    # 点击投放/取消投放按钮
    def click_audio_delivery_button(self):
        return self.scheduled_pushing_page.find_audio_delivery_button().click()

    # 点击编辑按钮
    def click_audio_edit_button(self):
        return self.scheduled_pushing_page.find_audio_edit_button().click()

    """
    以下操作用于验证操作结果是否正确
    """

    # 取数据内容类型列内容
    def get_table_content_type(self):
        return self.scheduled_pushing_page.find_table_content_type().text

    # 取数据投放id列内容
    def get_table_oid(self):
        return self.scheduled_pushing_page.find_table_oid().text

    # 取数据标题列内容
    def get_table_title(self):
        return self.scheduled_pushing_page.find_table_title().text

    # 取数据投放位置列内容
    def get_table_delivery_position(self):
        return self.scheduled_pushing_page.find_table_delivery_position().text

    # 取数据备注列内容
    def get_table_remark(self):
        return self.scheduled_pushing_page.find_table_remark().text

    # 取数据状态列内容
    def get_table_status(self):
        return self.scheduled_pushing_page.find_table_status().text

    # 获取成功弹窗
    def get_success_toast(self):
        return self.scheduled_pushing_page.find_success_toast().text

    # 取数据投放uid列内容
    def get_audio_uid(self):
        return self.scheduled_pushing_page.find_feed_uid().text

    # 取数据音频标题列内容
    def get_audio_title(self):
        return self.scheduled_pushing_page.find_audio_title().text

    # 取数据投放位置列内容
    def get_audio_delivery_position(self):
        return self.scheduled_pushing_page.find_audio_delivery_position().text

    # 取数据备注列内容
    def get_audio_remark(self):
        return self.scheduled_pushing_page.find_audio_remark().text

    # 取数据状态列内容
    def get_audio_status(self):
        return self.scheduled_pushing_page.find_audio_status().text


# 定投管理场景
class ScheduledPushingScenarios(object):
    def __init__(self, driver):
        self.scheduled_pushing_oper = ScheduledPushingOper(driver)

    """
    以下为新闻定投页场景
    """

    # 增加一条新数据
    def news_add_modal(self, cids, oid, channel_value, location, weight, remark):
        self.scheduled_pushing_oper.click_add_modal_button()
        sleep(5)
        self.scheduled_pushing_oper.click_cids_label()
        self.scheduled_pushing_oper.input_new_oid(oid)
        self.scheduled_pushing_oper.input_cids(cids)
        self.scheduled_pushing_oper.select_channel(channel_value)
        self.scheduled_pushing_oper.input_location(location)
        self.scheduled_pushing_oper.input_weight(weight)
        self.scheduled_pushing_oper.input_remark(remark)
        self.scheduled_pushing_oper.click_delivery_time()
        sleep(3)
        self.scheduled_pushing_oper.input_end_time_hour()
        sleep(3)
        self.scheduled_pushing_oper.input_end_time_minute()
        self.scheduled_pushing_oper.click_save_button()

    # 编辑之前新增的数据，只改备注
    def news_modify_modal(self, remark):
        self.scheduled_pushing_oper.click_table_edit_button()
        sleep(5)
        self.scheduled_pushing_oper.input_remark(remark)
        self.scheduled_pushing_oper.click_save_button()

    # 数据投放/取消投放
    def news_data_delivery(self):
        self.scheduled_pushing_oper.click_table_delivery_button()

    """
    以下为音频定投页场景
    """

    # 增加一条新数据
    def audio_add_modal(self, cids, uid, channel_value, location, weight, remark):
        self.scheduled_pushing_oper.click_add_modal_button()
        sleep(10)
        self.scheduled_pushing_oper.click_cids_label()
        self.scheduled_pushing_oper.input_new_uid(uid)
        self.scheduled_pushing_oper.input_cids(cids)
        self.scheduled_pushing_oper.select_channel(channel_value)
        self.scheduled_pushing_oper.input_location(location)
        self.scheduled_pushing_oper.input_weight(weight)
        self.scheduled_pushing_oper.input_remark(remark)
        self.scheduled_pushing_oper.click_delivery_time()
        sleep(3)
        self.scheduled_pushing_oper.input_end_time_hour()
        sleep(3)
        self.scheduled_pushing_oper.input_end_time_minute()
        self.scheduled_pushing_oper.click_save_button()
        sleep(5)
        self.scheduled_pushing_oper.input_operator()
        self.scheduled_pushing_oper.click_search_content_button()

    # 编辑之前新增的数据，只改备注
    def audio_modify_modal(self, remark):
        self.scheduled_pushing_oper.input_operator()
        self.scheduled_pushing_oper.click_search_content_button()
        sleep(3)
        self.scheduled_pushing_oper.click_audio_edit_button()
        sleep(3)
        self.scheduled_pushing_oper.input_remark(remark)
        self.scheduled_pushing_oper.click_save_button()

    # 数据投放/取消投放
    def audio_data_delivery(self):
        self.scheduled_pushing_oper.input_operator()
        self.scheduled_pushing_oper.click_search_content_button()
        sleep(3)
        self.scheduled_pushing_oper.click_audio_delivery_button()
