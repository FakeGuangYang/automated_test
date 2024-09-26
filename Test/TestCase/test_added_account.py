# -*- utf-8 -*-
# @Create Data: 2024/5/13 10:56
# @Author: guangyang219579
# @File: test_added_account.py

from selenium import webdriver
import pytest
from Test.PageObject import added_account_page
from Common.parse_yml import parse_yml
from Common.login import login
from Common.chrome_options import chrome_options
from time import sleep
from Common.result_matching import matchImgByTemplate
from get_script_directory import get_script_directory

# 已添加用户页url
host = parse_yml("/Config/login.yml", 'websites', 'host')
url = "http://" + host + "/mrd-operation/account/focus_account"


class TestAddedAccount():
    def setup(self):
        self.driver = webdriver.Chrome(options=chrome_options())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        login(self.driver)

    def test_search_name(self):
        # 进入已添加用户页
        self.driver.get(url)
        sleep(5)
        # 搜索的帐号昵称，可修改
        name = "航空及武器装备随笔"
        # 做搜索帐号昵称的操作
        added_account_page.AddedAccountScenarios(self.driver).search_name(name)
        sleep(5)
        # 获取界面数据结果
        res = self.driver.get_screenshot_as_base64()
        # 校验结果横坐标是否找到
        assert matchImgByTemplate(res, "/ResultPic/test_added_account.png")[0] != -1

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(
        ['-s', 'test_added_account.py', "--alluredir=" + get_script_directory() + "/Report/report"])
