# -*- utf-8 -*-
# @Create Data: 2022/5/26 10:27
# @Author: guangyang219579
# @File: test_login.py

from selenium import webdriver
import pytest
from Test.PageObject import login_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from Common.chrome_options import chrome_options

data = parse_csv("/Data/test_login.csv")
url = parse_yml("/Config/login.yml", 'websites', 'loginPage')


@pytest.mark.parametrize(("username", "password", "status"), data)
class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome(options=chrome_options())
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
            page_source = self.driver.page_source
            assert "autotestsup@sohu-inc.com" in page_source
        else:
            raise "ERROR: Status can only be 0 or 1."

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(['-s', 'test_login.py'])
