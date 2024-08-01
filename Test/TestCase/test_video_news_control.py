# -*- utf-8 -*-
# @Create Data: 2022/7/12 15:48
# @Author: guangyang219579
# @File: test_video_news_control.py

from selenium import webdriver
import pytest
from Test.PageObject import video_news_control_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from Common.chrome_options import chrome_options
from Common.delivery_time import delivery_time
from Common.login import login
from time import sleep

# 引用测试数据
data = parse_csv("../../Data/test_video_news_control_delivery_video.csv")
# 视频运营页url
host = parse_yml("../../Config/login.yml", 'websites', 'host')
url = "http://" + host + "/operation/videos/video_news_control_all"
# 停留时间
sleep_time = 2


class TestNewsScheduledPushing:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        login(self.driver)

    @pytest.mark.parametrize("oid", data)
    def test_delivery_video(self, oid):
        try:
            # 进入视频运营页
            self.driver.get(url)
            sleep(sleep_time)
            # 做投放操作
            video_news_control_page.VideoNewsControlScenarios(self.driver).delivery_video(oid, delivery_time())
            sleep(sleep_time)
        except Exception as e:
            print("Except: ", e)
        # 获取页面数据结果
        table_oid = video_news_control_page.VideoNewsControlOper(self.driver).get_table_oid()
        status = video_news_control_page.VideoNewsControlOper(self.driver).get_table_delivery_button_status()
        # 校验
        assert table_oid == oid
        assert status == "已投放"

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(['-s', 'test_video_news_control.py'])
