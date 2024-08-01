# -*- utf-8 -*-
# @Create Data: 2022/6/22 15:19
# @Author: guangyang219579
# @File: test_video_operation.py

from selenium import webdriver
import pytest
from Test.PageObject import video_operation_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from Common.chrome_options import chrome_options
from Common.delivery_time import delivery_time
from Common.login import login
from time import sleep

# 引用测试数据
add_content_data = parse_csv("../../Data/test_video_operation_add_content.csv")
edit_content_data = parse_csv("../../Data/test_video_operation_edit_content.csv")
# 登录页url
login_url = parse_yml("../../Config/login.yml", 'websites', 'loginPage')
# 视频运营页url
host = parse_yml("../../Config/login.yml", 'websites', 'host')
url = "http://" + host + "/operation/video/operation/toContentOperationList"
# 登录信息
username = parse_yml("../../Config/login.yml", 'loginInfo', 'username')
password = parse_yml("../../Config/login.yml", 'loginInfo', 'password')
# 停留时间
sleep_time = 2


class TestNewsScheduledPushing:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        login(self.driver)

    @pytest.mark.parametrize(("newsid", "tag", "priority_value"), add_content_data)
    def test_add_content(self, newsid, tag, priority_value):
        try:
            # 进入视频运营页
            self.driver.get(url)
            sleep(sleep_time)
            # 做添加数据操作
            video_operation_page.VideoOperationScenarios(self.driver).add_content(newsid, delivery_time(), tag,
                                                                                  priority_value)
            sleep(sleep_time)
        except Exception as e:
            print("Except: " + e)
        # 获取页面数据结果
        table_newsid = video_operation_page.VideoOperationOper(self.driver).get_table_newsid()
        title = video_operation_page.VideoOperationOper(self.driver).get_table_title()
        priority = video_operation_page.VideoOperationOper(self.driver).get_table_priority()
        tags = video_operation_page.VideoOperationOper(self.driver).get_table_tags()
        # 校验
        assert table_newsid == newsid
        assert title == "为充面子“衣锦还乡”小伙给宝马贴上“公务用车”标识被警方查获"
        assert priority == "高时效"
        assert "自动化测试" in tags

    @pytest.mark.parametrize("new_tag", edit_content_data)
    def test_edit_content(self, new_tag):
        # 进入视频运营页
        self.driver.get(url)
        sleep(sleep_time)
        # 做添加数据操作
        video_operation_page.VideoOperationScenarios(self.driver).edit_content(new_tag)
        sleep(sleep_time)
        # 获取页面数据结果
        title = video_operation_page.VideoOperationOper(self.driver).get_table_title()
        tags = video_operation_page.VideoOperationOper(self.driver).get_table_tags()
        # 校验
        assert title == "为充面子“衣锦还乡”小伙给宝马贴上“公务用车”标识被警方查获"
        assert "自动化测试-编辑后" in tags

    def test_remove_content(self):
        # 进入视频运营页
        self.driver.get(url)
        sleep(sleep_time)
        # 做添加数据操作
        video_operation_page.VideoOperationScenarios(self.driver).remove_content()
        sleep(sleep_time)
        # 获取页面数据结果
        empty_content = video_operation_page.VideoOperationOper(self.driver).get_table_newsid()
        # 校验
        assert empty_content == "没有相关记录"

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(['-s', 'test_video_operation.py'])
