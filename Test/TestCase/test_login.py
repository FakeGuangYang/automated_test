# -*- utf-8 -*-
# @Create Data: 2022/5/26 10:27
# @Author: guangyang219579
# @File: test_login.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from Test.PageObject import login_page
from Common.parse_csv import parse_csv
from time import sleep

data = parse_csv("Data/test_login.csv")
url = "https://sso.sohu-inc.com/login?service=http://opt.mrd.sohuno.com/operation/ssoValidate?returnUrl=/"
# 在Linux运行时需要添加Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('blink-settings=imagesEnabled=false')


@pytest.mark.parametrize(("username", "password", "status"), data)
class TestLogin():
    def setup(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)

    def test_login(self, username, password, status):
        login_page.LoginScenarios(self.driver).login(username, password)
        if status == '0':
            text = login_page.LoginOper(self.driver).get_login_failed_info()
            assert text == '登录失败！请输入有效的用户名/密码。'
        # TODO: 使用"find_element"方法取到的用户名是空，后续需要研究原因(可能是因为需要sleep?)
        elif status == '1':
            # page_source = self.driver.page_source
            # assert "guangyang219579@sohu-inc.com" in page_source
            sleep(10)
            login_name = login_page.LoginOper(self.driver).get_login_name()
            assert login_name == "guangyang219579"
        else:
            print("ERROR: Status can only be 0 or 1.")

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(['-s', 'test_login.py'])
