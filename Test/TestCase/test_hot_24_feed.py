# -*- utf-8 -*-
# @Create Data: 2022/8/24 16:13
# @Author: guangyang219579
# @File: test_hot_24_feed.py

from selenium import webdriver
import pytest
import pandas as pd
from Test.PageObject import login_page, hot_24_feed_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from Common.chrome_options import chrome_options
from time import sleep

# 引用测试数据
textli_data = parse_csv("Data/test_add_textli.csv")
picli_data = parse_csv("Data/test_add_picli.csv")
videoli_data = parse_csv("Data/test_add_videoli.csv")
linkli_data = parse_csv("Data/test_add_linkli.csv")
sohuvideoli_data = parse_csv("Data/test_add_sohuvideoli.csv")
listenli_data = parse_csv("Data/test_add_listenli.csv")
# 登录页url
login_url = parse_yml("Config/login.yml", 'websites', 'loginPage')
# 24小时feed页url
host = parse_yml("Config/login.yml", 'websites', 'host')
feed_url = "http://" + host + "/testhotred/hot24feed/toHot24FeedList"
page_url = "http://" + host + "/testhotred/hot24feed/toSelectedPage?go="
# 登录信息
username = parse_yml("Config/login.yml", 'loginInfo', 'username')
password = parse_yml("Config/login.yml", 'loginInfo', 'password')
# 通用参数
page = {"纯文字": "text", "文字+图片": "pic", "文字+视频": "video", "文字+外链": "link", "搜狐视频直播呼起": "sohuVideo", "真人播报": "listen"}
status = {"发布": "0", "撤回": "1", "前端删除": "2", "审核删除": "3", "后台删除": "4"}
feedtype = {"纯文字": "1", "文字+图片": "2", "文字+视频": "3", "文字+外链": "4", "搜狐视频直播呼起": "5", "真人播报": "6"}


# 纯文字
class TestTextHot24Feed():
    def setup(self):
        self.driver = webdriver.Chrome(options=chrome_options())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(login_url)
        # 登录
        login_page.LoginScenarios(self.driver).login(username, password)

    @pytest.mark.parametrize(("content", "view_time"), [textli_data[0][:2]])
    def test_add_textli(self, content, view_time):
        # 进入"创建新消息-纯文字"页
        self.driver.get(page_url + page["纯文字"])
        sleep(1)
        # 创建纯文字消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).add_textli(content, view_time)
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索新创建的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_new_data(status["发布"], feedtype["纯文字"])
        sleep(2)
        # 将生成的新数据存到文件中以供后续使用
        content_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_id()
        data_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_id_attribute()
        df = pd.read_csv("Data/test_add_textli.csv", delimiter=",")
        df['content_id'] = content_id
        df['id'] = data_id
        df.to_csv("Data/test_add_textli.csv", index=False, encoding="utf-8")
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "纯文字"
        assert table_content == "【拜登下令对叙利亚境内与伊朗有关的目标进行空袭】据美国有线电视新闻网和美联社报道，当地时间8月23日，美国总统拜登下令对叙利亚境内与伊朗有关的目标进行空袭。"
        assert data_status == "发布"
        assert important == "是"

    def test_edit_textli(self):
        data_id = pd.read_csv("Data/test_add_textli.csv", delimiter=",").iloc[0, 3]
        content_id = pd.read_csv("Data/test_add_textli.csv", delimiter=",").iloc[0, 2]
        # 进入当前id编辑页
        self.driver.get(page_url + page["纯文字"] + "&id=" + str(data_id))
        sleep(1)
        # 编辑消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).edit_data()
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索编辑的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(3)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "纯文字"
        assert table_content == "【拜登下令对叙利亚境内与伊朗有关的目标进行空袭】据美国有线电视新闻网和美联社报道，当地时间8月23日，美国总统拜登下令对叙利亚境内与伊朗有关的目标进行空袭。"
        assert data_status == "发布"
        assert important == "否"

    def test_recall_textli(self):
        content_id = pd.read_csv("Data/test_add_textli.csv", delimiter=",").iloc[0, 2]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 撤回消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).recall_data()
        sleep(2)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "纯文字"
        assert table_content == "【拜登下令对叙利亚境内与伊朗有关的目标进行空袭】据美国有线电视新闻网和美联社报道，当地时间8月23日，美国总统拜登下令对叙利亚境内与伊朗有关的目标进行空袭。"
        assert data_status == "撤回"
        assert important == "否"

    def test_delete_textli(self):
        content_id = pd.read_csv("Data/test_add_textli.csv", delimiter=",").iloc[0, 2]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 删除消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).delete_data()
        sleep(2)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "纯文字"
        assert table_content == "【拜登下令对叙利亚境内与伊朗有关的目标进行空袭】据美国有线电视新闻网和美联社报道，当地时间8月23日，美国总统拜登下令对叙利亚境内与伊朗有关的目标进行空袭。"
        assert data_status == "后台删除"
        assert important == "否"

    def teardown(self):
        self.driver.quit()


# 文字+图片
class TestPicHot24Feed():
    def setup(self):
        self.driver = webdriver.Chrome(options=chrome_options())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(login_url)
        # 登录
        login_page.LoginScenarios(self.driver).login(username, password)

    @pytest.mark.parametrize(("content", "pic", "view_time"), [picli_data[0][:3]])
    def test_add_picli(self, content, pic, view_time):
        # 进入"创建新消息-文字+图片"页
        self.driver.get(page_url + page["文字+图片"])
        sleep(1)
        # 创建文字+图片消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).add_picli(content, pic, view_time)
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索新创建的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_new_data(status["发布"], feedtype["文字+图片"])
        sleep(2)
        # 将生成的新数据存到文件中以供后续使用
        content_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_id()
        data_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_id_attribute()
        df = pd.read_csv("Data/test_add_picli.csv", delimiter=",")
        df['content_id'] = content_id
        df['id'] = data_id
        df.to_csv("Data/test_add_picli.csv", index=False, encoding="utf-8")
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "文字+图片"
        assert table_content == "【拜登下令对叙利亚境内与伊朗有关的目标进行空袭】据美国有线电视新闻网和美联社报道，当地时间8月23日，美国总统拜登下令对叙利亚境内与伊朗有关的目标进行空袭。"
        assert data_status == "发布"
        assert important == "是"

    def test_edit_picli(self):
        data_id = pd.read_csv("Data/test_add_picli.csv", delimiter=",").iloc[0, 4]
        content_id = pd.read_csv("Data/test_add_picli.csv", delimiter=",").iloc[0, 3]
        # 进入当前id编辑页
        self.driver.get(page_url + page["文字+图片"] + "&id=" + str(data_id))
        sleep(1)
        # 编辑消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).edit_pic_data()
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索编辑的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(3)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "文字+图片"
        assert table_content == "【拜登下令对叙利亚境内与伊朗有关的目标进行空袭】据美国有线电视新闻网和美联社报道，当地时间8月23日，美国总统拜登下令对叙利亚境内与伊朗有关的目标进行空袭。"
        assert data_status == "发布"
        assert important == "否"

    def test_recall_picli(self):
        content_id = pd.read_csv("Data/test_add_picli.csv", delimiter=",").iloc[0, 3]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 撤回消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).recall_data()
        sleep(2)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "文字+图片"
        assert table_content == "【拜登下令对叙利亚境内与伊朗有关的目标进行空袭】据美国有线电视新闻网和美联社报道，当地时间8月23日，美国总统拜登下令对叙利亚境内与伊朗有关的目标进行空袭。"
        assert data_status == "撤回"
        assert important == "否"

    def test_delete_picli(self):
        content_id = pd.read_csv("Data/test_add_picli.csv", delimiter=",").iloc[0, 3]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 删除消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).delete_data()
        sleep(2)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "文字+图片"
        assert table_content == "【拜登下令对叙利亚境内与伊朗有关的目标进行空袭】据美国有线电视新闻网和美联社报道，当地时间8月23日，美国总统拜登下令对叙利亚境内与伊朗有关的目标进行空袭。"
        assert data_status == "后台删除"
        assert important == "否"

    def teardown(self):
        self.driver.quit()


# 文字+视频
class TestVideoHot24Feed():
    def setup(self):
        self.driver = webdriver.Chrome(options=chrome_options())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(login_url)
        # 登录
        login_page.LoginScenarios(self.driver).login(username, password)

    @pytest.mark.parametrize(("content", "oid", "view_time"), [videoli_data[0][:3]])
    def test_add_videoli(self, content, oid, view_time):
        # 进入"创建新消息-文字+视频"页
        self.driver.get(page_url + page["文字+视频"])
        sleep(1)
        # 创建文字+视频消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).add_videoli(content, oid, view_time)
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(45)
        # 搜索新创建的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_new_data(status["发布"], feedtype["文字+视频"])
        sleep(1)
        # 将生成的新数据存到文件中以供后续使用
        content_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_id()
        data_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_id_attribute()
        df = pd.read_csv("Data/test_add_videoli.csv", delimiter=",")
        df['content_id'] = content_id
        df['id'] = data_id
        df.to_csv("Data/test_add_videoli.csv", index=False, encoding="utf-8")
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "文字+视频"
        assert table_content == "【拜登下令对叙利亚境内与伊朗有关的目标进行空袭】据美国有线电视新闻网和美联社报道，当地时间8月23日，美国总统拜登下令对叙利亚境内与伊朗有关的目标进行空袭。"
        assert data_status == "发布"
        assert important == "是"

    def test_edit_videoli(self):
        data_id = pd.read_csv("Data/test_add_videoli.csv", delimiter=",").iloc[0, 4]
        content_id = pd.read_csv("Data/test_add_videoli.csv", delimiter=",").iloc[0, 3]
        # 进入当前id编辑页
        self.driver.get(page_url + page["文字+视频"] + "&id=" + str(data_id))
        sleep(1)
        # 编辑消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).edit_data()
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索编辑的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(3)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "文字+视频"
        assert table_content == "【拜登下令对叙利亚境内与伊朗有关的目标进行空袭】据美国有线电视新闻网和美联社报道，当地时间8月23日，美国总统拜登下令对叙利亚境内与伊朗有关的目标进行空袭。"
        assert data_status == "发布"
        assert important == "否"

    def test_recall_videoli(self):
        content_id = pd.read_csv("Data/test_add_videoli.csv", delimiter=",").iloc[0, 3]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 撤回消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).recall_data()
        sleep(2)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "文字+视频"
        assert table_content == "【拜登下令对叙利亚境内与伊朗有关的目标进行空袭】据美国有线电视新闻网和美联社报道，当地时间8月23日，美国总统拜登下令对叙利亚境内与伊朗有关的目标进行空袭。"
        assert data_status == "撤回"
        assert important == "否"

    def test_delete_videoli(self):
        content_id = pd.read_csv("Data/test_add_videoli.csv", delimiter=",").iloc[0, 3]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 删除消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).delete_data()
        sleep(2)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "文字+视频"
        assert table_content == "【拜登下令对叙利亚境内与伊朗有关的目标进行空袭】据美国有线电视新闻网和美联社报道，当地时间8月23日，美国总统拜登下令对叙利亚境内与伊朗有关的目标进行空袭。"
        assert data_status == "后台删除"
        assert important == "否"

    def teardown(self):
        self.driver.quit()


# 文字+外链
class TestLinkHot24Feed():
    def setup(self):
        self.driver = webdriver.Chrome(options=chrome_options())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(login_url)
        # 登录
        login_page.LoginScenarios(self.driver).login(username, password)

    @pytest.mark.parametrize(("content", "oid", "view_time"), [linkli_data[0][:3]])
    def test_add_linkli(self, content, oid, view_time):
        # 进入"创建新消息-文字+外链"页
        self.driver.get(page_url + page["文字+外链"])
        sleep(1)
        # 创建文字+外链消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).add_linkli(content, oid, view_time)
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(2)
        # 搜索新创建的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_new_data(status["发布"], feedtype["文字+外链"])
        sleep(1)
        # 将生成的新数据存到文件中以供后续使用
        content_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_id()
        data_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_id_attribute()
        df = pd.read_csv("Data/test_add_linkli.csv", delimiter=",")
        df['content_id'] = content_id
        df['id'] = data_id
        df.to_csv("Data/test_add_linkli.csv", index=False, encoding="utf-8")
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        link_title = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_link_title()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "文字+外链"
        assert table_content == "海南疫情发布会，海南疫情发布会"
        assert link_title == "重庆北碚山火阻击战中的西南大学师生：外教组装油锯，老师参与灭火"
        assert data_status == "发布"
        assert important == "是"

    def test_edit_linkli(self):
        data_id = pd.read_csv("Data/test_add_linkli.csv", delimiter=",").iloc[0, 4]
        content_id = pd.read_csv("Data/test_add_linkli.csv", delimiter=",").iloc[0, 3]
        # 进入当前id编辑页
        self.driver.get(page_url + page["文字+外链"] + "&id=" + str(data_id))
        sleep(2)
        # 编辑消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).edit_link_data()
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索编辑的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(3)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "文字+外链"
        assert table_content == "海南疫情发布会，海南疫情发布会"
        assert data_status == "发布"
        assert important == "否"

    def test_recall_linkli(self):
        content_id = pd.read_csv("Data/test_add_linkli.csv", delimiter=",").iloc[0, 3]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 撤回消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).recall_data()
        sleep(2)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "文字+外链"
        assert table_content == "海南疫情发布会，海南疫情发布会"
        assert data_status == "撤回"
        assert important == "否"

    def test_delete_linkli(self):
        content_id = pd.read_csv("Data/test_add_linkli.csv", delimiter=",").iloc[0, 3]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 删除消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).delete_data()
        sleep(2)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "文字+外链"
        assert table_content == "海南疫情发布会，海南疫情发布会"
        assert data_status == "后台删除"
        assert important == "否"

    def teardown(self):
        self.driver.quit()


"""
# 搜狐视频直播呼起，运营已经停止使用
class TestSohuvideoHot24Feed():
    def setup(self):
        self.driver = webdriver.Chrome(options=chrome_options())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(login_url)
        # 登录
        login_page.LoginScenarios(self.driver).login(username, password)

    @pytest.mark.parametrize(("link_title", "link", "content", "pic", "view_time"), [sohuvideoli_data[0][:5]])
    def test_add_sohuvideoli(self, link_title, link, content, pic, view_time):
        # 进入"创建新消息-搜狐视频直播呼起"页
        self.driver.get(page_url + page["搜狐视频直播呼起"])
        sleep(1)
        # 创建搜狐视频直播呼起消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).add_sohuvideoli(link_title, link, content, pic, view_time)
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(2)
        # 搜索新创建的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_new_data(status["发布"], feedtype["搜狐视频直播呼起"])
        sleep(1)
        # 将生成的新数据存到文件中以供后续使用
        content_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_id()
        data_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_id_attribute()
        df = pd.read_csv("Data/test_add_sohuvideoli.csv", delimiter=",")
        df['content_id'] = content_id
        df['id'] = data_id
        df.to_csv("Data/test_add_sohuvideoli.csv", index=False, encoding="utf-8")
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        link_title = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_link_title()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "搜狐视频直播呼起"
        assert table_content == "海南疫情发布会，海南疫情发布会"
        assert link_title == "海南疫情发布会"
        assert data_status == "发布"
        assert important == "是"

    def test_edit_sohuvideoli(self):
        data_id = pd.read_csv("Data/test_add_sohuvideoli.csv", delimiter=",").iloc[0, 6]
        content_id = pd.read_csv("Data/test_add_sohuvideoli.csv", delimiter=",").iloc[0, 5]
        # 进入当前id编辑页
        self.driver.get(page_url + page["搜狐视频直播呼起"] + "&id=" + str(data_id))
        sleep(2)
        # 编辑消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).edit_sohuvideo_data()
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索编辑的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(3)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "搜狐视频直播呼起"
        assert table_content == "海南疫情发布会，海南疫情发布会"
        assert data_status == "发布"
        assert important == "否"

    def test_recall_sohuvideoli(self):
        content_id = pd.read_csv("Data/test_add_sohuvideoli.csv", delimiter=",").iloc[0, 5]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 撤回消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).recall_data()
        sleep(2)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "搜狐视频直播呼起"
        assert table_content == "海南疫情发布会，海南疫情发布会"
        assert data_status == "撤回"
        assert important == "否"

    def test_delete_linkli(self):
        content_id = pd.read_csv("Data/test_add_sohuvideoli.csv", delimiter=",").iloc[0, 5]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 删除消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).delete_data()
        sleep(2)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "搜狐视频直播呼起"
        assert table_content == "海南疫情发布会，海南疫情发布会"
        assert data_status == "后台删除"
        assert important == "否"

    def teardown(self):
        self.driver.quit()
"""


# 真人播报
class TestListenHot24Feed():
    def setup(self):
        self.driver = webdriver.Chrome(options=chrome_options())
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(login_url)
        # 登录
        login_page.LoginScenarios(self.driver).login(username, password)

    @pytest.mark.parametrize(("oid", "content", "view_time"), [listenli_data[0][:3]])
    def test_add_listenli(self, oid, content, view_time):
        # 进入"创建新消息-真人播报"页
        self.driver.get(page_url + page["真人播报"])
        sleep(1)
        # 创建真人播报消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).add_listenli(oid, content, view_time)
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(2)
        # 搜索新创建的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_new_data(status["发布"], feedtype["真人播报"])
        sleep(1)
        # 将生成的新数据存到文件中以供后续使用
        content_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_id()
        data_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_id_attribute()
        df = pd.read_csv("Data/test_add_listenli.csv", delimiter=",")
        df['content_id'] = content_id
        df['id'] = data_id
        df.to_csv("Data/test_add_listenli.csv", index=False, encoding="utf-8")
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        link_title = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_link_title()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "边看边听"
        assert table_content == "美印这次联合军演，果然藏着对华小动作"
        assert link_title == "美印这次联合军演，果然藏着对华小动作"
        assert data_status == "发布"
        assert important == "是"

    def test_edit_listenli(self):
        data_id = pd.read_csv("Data/test_add_listenli.csv", delimiter=",").iloc[0, 4]
        content_id = pd.read_csv("Data/test_add_listenli.csv", delimiter=",").iloc[0, 3]
        # 进入当前id编辑页
        self.driver.get(page_url + page["真人播报"] + "&id=" + str(data_id))
        sleep(2)
        # 编辑消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).edit_data()
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索编辑的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(3)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "边看边听"
        assert table_content == "美印这次联合军演，果然藏着对华小动作"
        assert data_status == "发布"
        assert important == "否"

    def test_recall_sohuvideoli(self):
        content_id = pd.read_csv("Data/test_add_listenli.csv", delimiter=",").iloc[0, 3]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 撤回消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).recall_data()
        sleep(2)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "边看边听"
        assert table_content == "美印这次联合军演，果然藏着对华小动作"
        assert data_status == "撤回"
        assert important == "否"

    def test_delete_linkli(self):
        content_id = pd.read_csv("Data/test_add_listenli.csv", delimiter=",").iloc[0, 3]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 删除消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).delete_data()
        sleep(2)
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type()
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content()
        data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status()
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important()
        # 校验
        assert content_type == "边看边听"
        assert table_content == "美印这次联合军演，果然藏着对华小动作"
        assert data_status == "后台删除"
        assert important == "否"

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(['-s', 'test_hot_24_feed.py'])
