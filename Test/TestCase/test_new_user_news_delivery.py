# -*- utf-8 -*-
# @Create Data: 2024/5/9 16:06
# @Author: guangyang219579
# @File: test_new_user_news_delivery.py

from selenium import webdriver
import pytest
from Test.PageObject import new_user_news_delivery_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from Common.login import login
from Common.chrome_options import chrome_options
from Common.delivery_time import delivery_time
from time import sleep
from Common.result_matching import matchImgByTemplate
from get_script_directory import get_script_directory

# 引用测试数据
data = parse_csv("/Data/test_new_user_news_delivery.csv")[0]
# 新用户文章投放页url
host = parse_yml("/Config/login.yml", 'websites', 'host')
url = "http://" + host + "/operation/operation/toNewUserArticleDelivery#"


class TestNewUserNewsDelivery():
    def setup(self):
        self.driver = webdriver.Chrome(chrome_options=chrome_options())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        login(self.driver)

    @pytest.mark.parametrize(("oid", "weight"), [data])
    def test_add_oid(self, oid, weight):
        # 进入新用户文章投放页
        self.driver.get(url)
        sleep(5)
        # 做添加oid的操作
        new_user_news_delivery_page.NewUserNewsDeliveryScenarios(self.driver).add_new_oid(oid, weight, delivery_time())
        sleep(5)
        # 获取界面数据结果
        res = self.driver.get_screenshot_as_base64()
        # 校验结果横坐标是否找到
        assert matchImgByTemplate(res, "/ResultPic/add_channel.png")[0] != -1

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(
        ['-s', 'test_new_user_news_delivery.py', "--alluredir=" + get_script_directory() + "/Report/allure-report"])
