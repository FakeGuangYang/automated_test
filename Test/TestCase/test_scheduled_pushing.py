# -*- utf-8 -*-
# @Create Data: 2022/6/9 09:53
# @Author: guangyang219579
# @File: test_scheduled_pushing.py

from selenium import webdriver
import pytest
from Test.PageObject import login_page, scheduled_pushing_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from Common.delivery_time import delivery_time
from Common.chrome_options import chrome_options
from time import sleep

# 引用测试数据
add_news_modal_data = parse_csv("Data/test_news_add_modal.csv")
add_audio_modal_data = parse_csv("Data/test_audio_add_modal.csv")
modify_modal_data = parse_csv("Data/test_modify_modal.csv")
# 登录页url
login_url = parse_yml("Config/login.yml", 'websites', 'loginPage')
# 定投管理页url
host = parse_yml("Config/login.yml", 'websites', 'host')
news = "http://" + host + "/operation/delivery/toTargetedDeliveryList?type=news"
audio = "http://" + host + "/operation/delivery/toTargetedDeliveryList?type=audio"
# 登录信息
username = parse_yml("Config/login.yml", 'loginInfo', 'username')
password = parse_yml("Config/login.yml", 'loginInfo', 'password')


class TestNewsScheduledPushing():
    def setup(self):
        self.driver = webdriver.Chrome(chrome_options())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(login_url)
        # 登录
        login_page.LoginScenarios(self.driver).login(username, password)

    @pytest.mark.parametrize(("cids", "oid", "channel_value", "location", "weight", "remark"), add_news_modal_data)
    def test_add_modal(self, cids, oid, channel_value, location, weight, remark):
        # 进入新闻定投页
        self.driver.get(news)
        sleep(5)
        # 做添加数据操作
        scheduled_pushing_page.ScheduledPushingScenarios(self.driver).news_add_modal(cids, oid, channel_value, location,
                                                                                     weight, remark, delivery_time())
        sleep(5)
        # 获取界面数据结果
        content_type = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_content_type()
        table_oid = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_oid()
        title = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_title()
        delivery_position = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_delivery_position()
        table_remark = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_remark()
        status = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_status()
        # 校验
        assert content_type == "普通"
        assert table_oid == oid
        assert title == "【社会主义核心价值观】友善 公民道德的基石"
        assert delivery_position == location
        assert table_remark == remark
        # 目前投放时间都是过去的时间因此都为已过期
        assert status == "已投放:\n已过期"

    @pytest.mark.parametrize("new_remark", modify_modal_data[0])
    def test_modify_modal(self, new_remark):
        # 进入新闻定投页
        self.driver.get(news)
        sleep(5)
        # 做编辑数据操作，仅修改备注
        scheduled_pushing_page.ScheduledPushingScenarios(self.driver).news_modify_modal(new_remark)
        sleep(5)
        # 获取界面数据结果
        table_remark = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_remark()
        status = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_status()
        # 校验
        assert table_remark == new_remark
        # 目前投放时间都是过去的时间因此都为已过期
        assert status == "已投放:\n已过期"

    def test_stop_delivery(self):
        # 进入新闻定投页
        self.driver.get(news)
        sleep(5)
        # 做取消投放操作
        scheduled_pushing_page.ScheduledPushingScenarios(self.driver).news_data_delivery()
        sleep(5)
        # 获取界面数据结果
        status = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_status()
        # 校验
        # 目前投放时间都是过去的时间因此都为已过期
        assert status == "待投放:\n已过期"

    def test_continue_delivery(self):
        # 进入新闻定投页
        self.driver.get(news)
        sleep(5)
        # 做投放操作
        scheduled_pushing_page.ScheduledPushingScenarios(self.driver).news_data_delivery()
        sleep(5)
        # 获取界面数据结果
        status = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_status()
        # 校验
        # 目前投放时间都是过去的时间因此都为已过期
        assert status == "已投放:\n已过期"

    def teardown(self):
        self.driver.quit()


class TestAudioScheduledPushing():
    def setup(self):
        self.driver = webdriver.Chrome(chrome_options())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(login_url)
        # 登录
        login_page.LoginScenarios(self.driver).login(username, password)

    @pytest.mark.parametrize(("cids", "uid", "channel_value", "location", "weight", "remark"), add_audio_modal_data)
    def test_add_modal(self, cids, uid, channel_value, location, weight, remark):
        # 进入音频定投页
        self.driver.get(audio)
        sleep(5)
        # 做添加数据操作
        scheduled_pushing_page.ScheduledPushingScenarios(self.driver).audio_add_modal(cids, uid, channel_value,
                                                                                      location, weight, remark,
                                                                                      delivery_time())
        sleep(5)
        # 获取界面数据结果
        table_uid = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_audio_uid()
        title = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_audio_title()
        delivery_position = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_audio_delivery_position()
        table_remark = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_audio_remark()
        status = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_audio_status()
        # 校验
        assert table_uid == "uid: " + uid
        assert title == '从神九到神十四，首位“飞天女”刘洋：心怀山海'
        assert delivery_position == location
        assert table_remark == remark
        # 目前投放时间都是过去的时间因此都为已过期
        assert status == "已投放:\n已过期"

    @pytest.mark.parametrize("new_remark", modify_modal_data[0])
    def test_modify_modal(self, new_remark):
        # 进入音频定投页
        self.driver.get(audio)
        sleep(5)
        # 做编辑数据操作，仅修改备注
        scheduled_pushing_page.ScheduledPushingScenarios(self.driver).audio_modify_modal(new_remark)
        sleep(5)
        # 获取界面数据结果
        table_remark = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_audio_remark()
        status = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_audio_status()
        # 校验
        assert table_remark == new_remark
        # 目前投放时间都是过去的时间因此都为已过期
        assert status == "已投放:\n已过期"

    def test_stop_delivery(self):
        # 进入音频定投页
        self.driver.get(audio)
        sleep(5)
        # 做取消投放操作
        scheduled_pushing_page.ScheduledPushingScenarios(self.driver).audio_data_delivery()
        sleep(5)
        # 获取界面数据结果
        status = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_audio_status()
        # 校验
        # 目前投放时间都是过去的时间因此都为已过期
        assert status == "待投放:\n已过期"

    def test_continue_delivery(self):
        # 进入音频定投页
        self.driver.get(audio)
        sleep(5)
        # 做投放操作
        scheduled_pushing_page.ScheduledPushingScenarios(self.driver).audio_data_delivery()
        sleep(5)
        # 获取界面数据结果
        status = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_audio_status()
        # 校验
        # 目前投放时间都是过去的时间因此都为已过期
        assert status == "已投放:\n已过期"

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(['-s', 'test_scheduled_pushing.py'])
