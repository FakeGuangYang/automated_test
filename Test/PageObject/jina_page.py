# -*- utf-8 -*-
# @Create Data: 2022/6/8 14:31
# @Author: guangyang219579
# @File: jina_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


# 集纳页对象
class JinaPage(object):
    def __init__(self, driver):
        self.driver = driver

    """
    以下为集纳页频道配置页中的元素
    """

    # "[新建]"按钮元素
    def find_add_button(self):
        ele = self.driver.find_element(By.XPATH, '//button[contains(.,"新建")]')
        return ele

    # "频道名称"输入框元素
    def find_channel_name_input(self):
        ele = self.driver.find_element(By.XPATH, '//div[contains(.,"频道名称")]/div/div/input')
        return ele

    # "频道类型 - 长期"选择框元素
    def find_channel_type_label(self):
        ele = self.driver.find_element(By.XPATH, '//label[contains(.,"长期")]')
        return ele

    # "权重"输入框元素
    def find_weight_input(self):
        ele = self.driver.find_element(By.XPATH, '//label[text()="权重"]/../div/div/div/input')
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "[确定]"按钮元素
    def find_channel_submit_button(self):
        ele = self.driver.find_element(By.XPATH, '//button[contains(.,"确 定")]')
        return ele

    # 编辑新闻页面"[确定]"按钮元素
    def find_modify_news_submit_button(self):
        ele = self.driver.find_element(By.XPATH,
                                       '//*[@aria-label="编辑新闻"]/div[@class="el-dialog__footer"]/'
                                       'div/button[contains(.,"确 定")]')
        return ele

    # 列表"频道类型"元素
    def find_table_channel_type(self, channel_name):
        path = '//div[text()="' + channel_name + '"]/../../td[2]/div/div'
        ele = self.driver.find_element(By.XPATH, path)
        return ele

    # 列表"权重"元素
    def find_table_channel_weight(self, channel_name):
        path = '//div[text()="' + channel_name + '"]/../../td[4]/div'
        ele = self.driver.find_element(By.XPATH, path)
        return ele

    # 列表"[修改]"按钮元素
    def find_table_channel_modify_button(self, channel_name):
        path = '//div[text()="' + channel_name + '"]/../../td[5]/div/button[contains(.,"修改")]'
        ele = self.driver.find_element(By.XPATH, path)
        return ele

    # 列表"[删除]"按钮元素
    def find_table_channel_delete_button(self, channel_name):
        path = '//div[text()="' + channel_name + '"]/../../td[5]/div/span/span/button'
        ele = self.driver.find_element(By.XPATH, path)
        return ele

    # 确认弹窗元素
    def find_popup_confirm_button(self):
        ele = self.driver.find_element(By.XPATH, '//div[@aria-hidden="false"]/div/div/button[2]')
        return ele

    """
    以下为集纳页新闻配置页中的元素
    """

    # "[频道配置]"按钮元素
    def find_channel_config_button(self):
        ele = self.driver.find_element(By.XPATH, '//button[contains(.,"频道配置")]')
        return ele

    # "频道"下拉框元素
    def find_news_channel_dropdown(self):
        path = '//label[contains(.,"频道")]/../div/div/div/input'
        ele = self.driver.find_element(By.XPATH, path)
        return ele

    # 选择刚创建频道元素
    def find_news_channel_button(self, channel_name):
        path = '//*[@class="el-scrollbar"]/div/ul/li/span[text()="' + channel_name + '"]/..'
        ele = self.driver.find_element(By.XPATH, path)
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # "oid"输入框元素
    def find_news_oid_input(self):
        ele = self.driver.find_element(By.XPATH, '//label[contains(.,"oid")]/../div/div/input')
        return ele

    # "[确定]"按钮元素
    def find_news_submit_button(self):
        ele = self.driver.find_element(By.XPATH,
                                       '//span[contains(.,"新建新闻")]/../../div[3]/div/button[contains(.,"确 定")]')
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, ele)
        return ele

    # 选择页面左侧的频道
    def find_channel_table_button(self, channel_name):
        path = '//div[@role="tablist"]/div[text()="' + channel_name + '(长期)"]'
        ele = self.driver.find_element(By.XPATH, path)
        return ele

    # 列表"标题"元素
    def find_table_news_title(self, oid):
        path = '//tr[contains(.,"' + oid + '")]/td[4]/div'
        ele = self.driver.find_element(By.XPATH, path)
        return ele

    # 列表"权重"元素
    def find_table_news_weight(self, oid):
        path = '//tr[contains(.,"' + oid + '")]/td[7]/div'
        ele = self.driver.find_element(By.XPATH, path)
        return ele

    # 列表"[修改]"按钮元素
    def find_table_news_modify_button(self, oid):
        path = '//tr[contains(.,"' + oid + '")]/td[11]/div/button'
        ele = self.driver.find_element(By.XPATH, path)
        return ele

    # 列表"[删除]"按钮元素
    def find_table_news_delete_button(self, oid):
        path = '//tr[contains(.,"' + oid + '")]/td[11]/div/span/span/button'
        ele = self.driver.find_element(By.XPATH, path)
        return ele

    # "[下线频道]"按钮元素
    def find_offline_channel_button(self):
        ele = self.driver.find_element(By.ID, "tab-offline")
        return ele


# 集纳页操作
class JinaOper(object):
    def __init__(self, driver):
        self.jina_page = JinaPage(driver)
        self.wait = WebDriverWait(driver, 10)

    """
    以下操作用于场景中，模拟用户操作
    """

    # 点击[添加]按钮
    def click_add_button(self):
        self.jina_page.find_add_button().click()

    # 输入频道名称
    def input_channel_name(self, channel_name):
        self.jina_page.find_channel_name_input().clear()
        self.jina_page.find_channel_name_input().send_keys(channel_name)

    # 点击[频道类型 - 长期]选择框
    def click_channel_type_label(self):
        self.jina_page.find_channel_type_label().click()

    # 输入权重
    def input_weight(self, weight):
        self.jina_page.find_weight_input().clear()
        self.jina_page.find_weight_input().send_keys(weight)

    # 点击频道[确定]按钮
    def click_channel_submit_button(self):
        self.jina_page.find_channel_submit_button().click()

    # 点击编辑新闻页面[确定]按钮
    def click_modify_news_submit_button(self):
        self.jina_page.find_modify_news_submit_button().click()

    # 点击频道[修改]按钮
    def click_channel_modify_button(self, channel_name):
        self.jina_page.find_table_channel_modify_button(channel_name).click()

    # 点击频道[删除]按钮
    def click_channel_delete_button(self, channel_name):
        self.jina_page.find_table_channel_delete_button(channel_name).click()

    # 点击确认弹窗[确定]按钮
    def click_popup_confirm_button(self):
        self.jina_page.find_popup_confirm_button().click()

    # 点击频道出现下拉框
    def click_news_channel_dropdown(self):
        self.jina_page.find_news_channel_dropdown().click()

    # 选择频道
    def click_news_channel(self, channel_name):
        self.jina_page.find_news_channel_button(channel_name).click()

    # 输入oid
    def input_news_oid(self, oid):
        self.jina_page.find_news_oid_input().clear()
        self.jina_page.find_news_oid_input().send_keys(oid)

    # 点击新闻[确定]按钮
    def click_news_submit_button(self):
        self.jina_page.find_news_submit_button().click()

    # 点击新闻[修改]按钮
    def click_news_modify_button(self, oid):
        self.jina_page.find_table_news_modify_button(oid).click()

    # 点击新闻[删除]按钮
    def click_news_delete_button(self, oid):
        self.jina_page.find_table_news_delete_button(oid).click()

    # 点击新建的频道以选择
    def click_channel_table_button(self, channel_name):
        self.jina_page.find_channel_table_button(channel_name).click()

    # 点击[下线频道]按钮
    def click_offline_channel_button(self):
        self.jina_page.find_offline_channel_button().click()

    """
    以下操作用于验证操作结果是否正确
    """

    # 取数据频道类型列内容
    def get_table_channel_type(self, channel_name):
        return self.jina_page.find_table_channel_type(channel_name).text

    # 取数据权重列内容
    def get_table_channel_weight(self, channel_name):
        return self.jina_page.find_table_channel_weight(channel_name).text

    # 取数据标题列内容
    def get_table_news_title(self, oid):
        return self.jina_page.find_table_news_title(oid).text

    # 取数据权重列内容
    def get_table_news_weight(self, oid):
        return self.jina_page.find_table_news_weight(oid).text


# 集纳页场景
class JinaScenarios(object):
    def __init__(self, driver):
        self.jina_oper = JinaOper(driver)

    # 新增频道
    def add_channel(self, channel_name):
        self.jina_oper.click_add_button()
        sleep(3)
        self.jina_oper.click_channel_type_label()
        self.jina_oper.input_channel_name(channel_name)
        self.jina_oper.click_channel_submit_button()

    # 修改频道
    def modify_channel(self, channel_name, weight):
        self.jina_oper.click_channel_modify_button(channel_name)
        sleep(3)
        self.jina_oper.input_weight(weight)
        self.jina_oper.click_channel_submit_button()

    # 删除频道
    def delete_channel(self, channel_name):
        self.jina_oper.click_channel_delete_button(channel_name)
        sleep(3)
        self.jina_oper.click_popup_confirm_button()

    # 新增新闻
    def add_news(self, channel_name, oid):
        self.jina_oper.click_add_button()
        sleep(3)
        self.jina_oper.input_news_oid(oid)
        self.jina_oper.click_news_channel_dropdown()
        sleep(3)
        self.jina_oper.click_news_channel(channel_name)
        self.jina_oper.click_news_submit_button()

    # 修改新闻
    def modify_news(self, channel_name, oid, weight):
        self.jina_oper.click_offline_channel_button()
        self.jina_oper.click_channel_table_button(channel_name)
        self.jina_oper.click_news_modify_button(oid)
        sleep(3)
        self.jina_oper.input_weight(weight)
        self.jina_oper.click_modify_news_submit_button()

    # 删除新闻
    def delete_news(self, channel_name, oid):
        self.jina_oper.click_offline_channel_button()
        self.jina_oper.click_channel_table_button(channel_name)
        self.jina_oper.click_news_delete_button(oid)
        sleep(3)
        self.jina_oper.click_popup_confirm_button()
