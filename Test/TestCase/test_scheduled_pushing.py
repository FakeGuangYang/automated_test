# -*- utf-8 -*-
# @Create Data: 2022/6/9 09:53
# @Author: guangyang219579
# @File: test_scheduled_pushing.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from Test.PageObject import login_page, scheduled_pushing_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from time import sleep

# 在Linux运行时需要添加Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('blink-settings=imagesEnabled=false')

# 引用测试数据
add_modal_data = parse_csv("Data/test_add_modal.csv")
modify_modal_data = parse_csv("Data/test_modify_modal.csv")
# 登录页url
login_url = "https://sso.sohu-inc.com/login?service=http://opt.mrd.sohuno.com/operation/ssoValidate?returnUrl=/"
# 定投管理页url
host = parse_yml("Config/login.yml", 'websites', 'host')
url = "http://" + host + "/operation/delivery/toTargetedDeliveryList"
# 登录信息
username = parse_yml("Config/login.yml", 'loginInfo', 'username')
password = parse_yml("Config/login.yml", 'loginInfo', 'password')


class TestScheduledPushing():
    def setup(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(login_url)
        # 登录
        login_page.LoginScenarios(self.driver).login(username, password)

    @pytest.mark.parametrize(("cids", "oid", "channel_value", "location", "weight", "remark"), add_modal_data)
    def test_add_modal(self, cids, oid, channel_value, location, weight, remark):
        # 进入定投管理页
        self.driver.get(url)
        # 做添加数据操作
        scheduled_pushing_page.ScheduledPushingScenarios(self.driver).add_modal(cids, oid, channel_value, location,
                                                                                weight, remark)
        sleep(3)
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
        assert status == "已投放"

    @pytest.mark.parametrize("new_remark", modify_modal_data[0])
    def test_modify_modal(self, new_remark):
        # 进入定投管理页
        self.driver.get(url)
        # 做编辑数据操作，仅修改备注
        scheduled_pushing_page.ScheduledPushingScenarios(self.driver).modify_modal(new_remark)
        sleep(3)
        # 获取界面数据结果
        table_remark = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_remark()
        status = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_status()
        # 校验
        assert table_remark == new_remark
        assert status == "已投放"

    def test_stop_delivery(self):
        # 进入定投管理页
        self.driver.get(url)
        # 做取消投放操作
        scheduled_pushing_page.ScheduledPushingScenarios(self.driver).data_delivery()
        sleep(3)
        # 获取界面数据结果
        status = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_status()
        # 校验
        assert status == "待投放"

    def test_continue_delivery(self):
        # 进入定投管理页
        self.driver.get(url)
        # 做投放操作
        scheduled_pushing_page.ScheduledPushingScenarios(self.driver).data_delivery()
        sleep(3)
        # 获取界面数据结果
        status = scheduled_pushing_page.ScheduledPushingOper(self.driver).get_table_status()
        # 校验
        assert status == "已投放"

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(['-s', 'test_scheduled_pushing.py'])
