# -*- utf-8 -*-
# @Create Data: 2022/5/25 13:28
# @Author: guangyang219579
# @File: login_page.py

from selenium.webdriver.common.by import By


# 登录页元素
class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver

    # "用户名输入框"元素
    def find_username(self):
        ele = self.driver.find_element(By.ID, 'userName')
        return ele

    # "密码输入框"元素
    def find_password(self):
        ele = self.driver.find_element(By.ID, 'pass')
        return ele

    # "登录按钮"元素
    def find_login_button(self):
        ele = self.driver.find_element(By.ID, 'loginBtn')
        return ele

    # "登录后登录名"元素
    def find_login_name(self):
        ele = self.driver.find_element(By.CLASS_NAME, 'email')
        return ele

    # "登录报错错误信息"元素
    def find_login_failed_info(self):
        ele = self.driver.find_element(By.ID, 'myError')
        return ele

    # "登陆后的url"元素
    def find_login_url(self):
        ele = self.driver.current_url
        return ele

    # "登陆后的url"元素
    def find_pic(self):
        ele = self.driver.find_element(By.XPATH, '//img')
        return ele


# 登录页操作
class LoginOper(object):
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    # 输入用户名
    def input_username(self, username):
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)

    # 输入密码
    def input_password(self, password):
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(password)

    # 点击登录按钮
    def click_login_button(self):
        self.login_page.find_login_button().click()

    # 获取登录名
    def get_login_name(self):
        return self.login_page.find_login_name().text

    # 获取登录失败信息
    def get_login_failed_info(self):
        return self.login_page.find_login_failed_info().text

    # 判断登陆后url是否需要再点击图片才能跳转到页面
    def click_pic(self):
        if "ssologin" in self.login_page.find_login_url():
            self.login_page.find_pic().click()
        else:
            pass


# 登录页场景
class LoginScenarios(object):
    def __init__(self, driver):
        self.login_oper = LoginOper(driver)

    # 登录
    def login(self, username, password):
        self.login_oper.input_username(username)
        self.login_oper.input_password(password)
        self.login_oper.click_login_button()
        self.login_oper.click_pic()
