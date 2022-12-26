# -*- utf-8 -*-
# @Create Data: 2022/12/12 11:06
# @Author: guangyang219579
# @File: test_jina.py

from selenium import webdriver
import pytest
from Test.PageObject import jina_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from Common.login import login
from Common.chrome_options import chrome_options
from time import sleep

# 引用测试数据
data = parse_csv("Data/test_jina_data.csv")[0]
# 定投管理页url
host = parse_yml("Config/login.yml", 'websites', 'host')
channel = "http://" + host + "/operation/jina/channel/index"
news = "http://" + host + "/operation/jina/news/index"


class TestJina():
    def setup(self):
        self.driver = webdriver.Chrome(options=chrome_options())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        login(self.driver)

    @pytest.mark.parametrize("channel_name", [data[0]])
    def test_add_channel(self, channel_name):
        # 进入频道配置页
        self.driver.get(channel)
        sleep(5)
        # 做添加频道操作
        jina_page.JinaScenarios(self.driver).add_channel(channel_name)
        sleep(5)
        # 获取界面数据结果
        channel_type = jina_page.JinaOper(self.driver).get_table_channel_type(channel_name)
        weight = jina_page.JinaOper(self.driver).get_table_channel_weight(channel_name)
        # 校验
        assert channel_type == "长期"
        assert weight == "0"

    @pytest.mark.parametrize(("channel_name", "channel_weight"), [data[:2]])
    def test_modify_channel(self, channel_name, channel_weight):
        # 进入频道配置页
        self.driver.get(channel)
        sleep(5)
        # 做修改频道操作
        jina_page.JinaScenarios(self.driver).modify_channel(channel_name, channel_weight)
        sleep(5)
        # 获取界面数据结果
        weight = jina_page.JinaOper(self.driver).get_table_channel_weight(channel_name)
        # 校验
        assert weight == channel_weight

    @pytest.mark.parametrize(("channel_name", "oid"), [[data[0], data[2]]])
    def test_add_news(self, channel_name, oid):
        # 进入新闻配置页
        self.driver.get(news)
        sleep(5)
        # 做添加新闻操作
        jina_page.JinaScenarios(self.driver).add_news(channel_name, oid)
        sleep(5)
        # 获取界面数据结果
        news_title = jina_page.JinaOper(self.driver).get_table_news_title(oid)
        news_weight = jina_page.JinaOper(self.driver).get_table_news_weight(oid)
        # 校验
        assert news_title == "这一幕激怒俄罗斯！"
        assert news_weight == "0"

    @pytest.mark.parametrize(("channel_name", "oid", "news_weight"), [[data[0], data[2], data[3]]])
    def test_modify_news(self, channel_name, oid, news_weight):
        # 进入新闻配置页
        self.driver.get(news)
        sleep(5)
        # 做修改新闻操作
        jina_page.JinaScenarios(self.driver).modify_news(channel_name, oid, news_weight)
        sleep(5)
        # 获取界面数据结果
        weight = jina_page.JinaOper(self.driver).get_table_news_weight(oid)
        # 校验
        assert weight == news_weight

    @pytest.mark.parametrize(("channel_name", "oid"), [[data[0], data[2]]])
    def test_delete_news(self, channel_name, oid):
        # 进入新闻配置页
        self.driver.get(news)
        sleep(5)
        # 做删除新闻操作
        jina_page.JinaScenarios(self.driver).delete_news(channel_name, oid)
        sleep(5)
        # 获取界面数据结果
        try:
            jina_page.JinaOper(self.driver).get_table_news_weight(oid)
        except Exception as e:
            # 校验
            assert "no such element" in str(e)

    @pytest.mark.parametrize("channel_name", [data[0]])
    def test_delete_channel(self, channel_name):
        # 进入频道配置页
        self.driver.get(channel)
        sleep(5)
        # 做删除频道操作
        jina_page.JinaScenarios(self.driver).delete_channel(channel_name)
        sleep(5)
        # 获取界面数据结果
        try:
            jina_page.JinaOper(self.driver).get_table_channel_weight(channel_name)
        except Exception as e:
            # 校验
            assert "no such element" in str(e)

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(['-s', 'test_jina.py'])
