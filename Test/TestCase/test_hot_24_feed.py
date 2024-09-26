# -*- utf-8 -*-
# @Create Data: 2022/8/24 16:13
# @Author: guangyang219579
# @File: test_hot_24_feed.py

from selenium import webdriver
import pytest
import pandas as pd
from Test.PageObject import hot_24_feed_page
from Common.parse_csv import parse_csv
from Common.parse_yml import parse_yml
from Common.login import login
from Common.chrome_options import chrome_options
from time import sleep

# 通用参数
page = {"纯文字": "text", "文字+图片": "pic", "文字+视频": "video", "文字+外链": "link", "搜狐视频直播呼起": "sohuVideo",
        "真人播报": "listen"}
status = {"发布": "0", "撤回": "1", "前端删除": "2", "审核删除": "3", "后台删除": "4"}
feedtype = {"纯文字": "1", "文字+图片": "2", "文字+视频": "3", "文字+外链": "4", "搜狐视频直播呼起": "5", "真人播报": "6"}

# 24小时feed页url
host = parse_yml("../../Config/login.yml", 'websites', 'host')
feed_url = "http://" + host + ":10510/testhotred/hot24feed/toHot24FeedList"
page_url = "http://" + host + ":10510/testhotred/hot24feed/toSelectedPage?go="

# 引用测试数据
textli_data = parse_csv("../../Data/test_add_textli.csv")
# picli_data = parse_csv("../../Data/test_add_picli.csv")
# videoli_data = parse_csv("../../Data/test_add_videoli.csv")
# linkli_data = parse_csv("../../Data/test_add_linkli.csv")
# listenli_data = parse_csv("../../Data/test_add_listenli.csv")


# 纯文字
class TestTextHot24Feed():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        login(self.driver)

    @pytest.mark.parametrize("content", [textli_data[0][0]])
    def test_add_textli(self, content):
        # 进入"创建新消息-纯文字"页
        self.driver.get(page_url + page["纯文字"])
        sleep(1)
        # 创建纯文字消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).add_textli(content)
        sleep(1)
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索新创建的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_new_data(status["撤回"], feedtype["纯文字"])
        sleep(2)
        # 将生成的新数据存到文件中以供后续使用
        content_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_id()
        data_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_id_attribute(content)
        df = pd.read_csv("../../Data/test_add_textli.csv", delimiter=",")
        df['content_id'] = content_id
        df['id'] = data_id
        df.to_csv("../../Data/test_add_textli.csv", index=False, encoding="utf-8")
        # 获取页面数据结果
        content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type(content_id)
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important(content_id)
        # 校验
        assert content_type == "纯文字"
        assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
        assert important == "否"

    def test_edit_textli(self):
        data_id = pd.read_csv("../../Data/test_add_textli.csv", delimiter=",").iloc[0, 2]
        content_id = pd.read_csv("../../Data/test_add_textli.csv", delimiter=",").iloc[0, 1]
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
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
        important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important(content_id)
        # 校验
        assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
        assert important == "是"

    def test_delete_textli(self):
        content_id = pd.read_csv("../../Data/test_add_textli.csv", delimiter=",").iloc[0, 1]
        # 进入24小时feed版本页
        self.driver.get(feed_url)
        sleep(1)
        # 搜索操作的消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
        sleep(2)
        # 删除消息
        hot_24_feed_page.Hot24FeedScenarios(self.driver).delete_data(content_id)
        sleep(2)
        # 获取页面数据结果
        table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
        table_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status(content_id)
        # 校验
        assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
        assert table_status == "后台删除"

    def teardown(self):
        self.driver.quit()


# 文字+图片
# class TestPicHot24Feed():
#     def setup(self):
#         self.driver = webdriver.Chrome(options=chrome_options())
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#         login(self.driver)
#
#     @pytest.mark.parametrize(("content", "pic"), [picli_data[0][:2]])
#     def test_add_picli(self, content, pic):
#         # 进入"创建新消息-文字+图片"页
#         self.driver.get(page_url + page["文字+图片"])
#         sleep(1)
#         # 创建文字+图片消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).add_picli(content, pic)
#         sleep(1)
#         # 进入24小时feed版本页
#         self.driver.get(feed_url)
#         sleep(1)
#         # 搜索新创建的消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).search_new_data(status["撤回"], feedtype["文字+图片"])
#         sleep(2)
#         # 将生成的新数据存到文件中以供后续使用
#         content_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_id()
#         data_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_id_attribute(content)
#         df = pd.read_csv("Data/test_add_picli.csv", delimiter=",")
#         df['content_id'] = content_id
#         df['id'] = data_id
#         df.to_csv("Data/test_add_picli.csv", index=False, encoding="utf-8")
#         # 获取页面数据结果
#         content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type(content_id)
#         table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
#         important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important(content_id)
#         # 校验
#         assert content_type == "文字+图片"
#         assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
#         assert important == "否"
#
#     def test_edit_picli(self):
#         data_id = pd.read_csv("Data/test_add_picli.csv", delimiter=",").iloc[0, 3]
#         content_id = pd.read_csv("Data/test_add_picli.csv", delimiter=",").iloc[0, 2]
#         # 进入当前id编辑页
#         self.driver.get(page_url + page["文字+图片"] + "&id=" + str(data_id))
#         sleep(1)
#         # 编辑消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).edit_data()
#         sleep(1)
#         # 进入24小时feed版本页
#         self.driver.get(feed_url)
#         sleep(1)
#         # 搜索编辑的消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
#         sleep(3)
#         # 获取页面数据结果
#         table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
#         important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important(content_id)
#         # 校验
#         assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
#         assert important == "是"
#
#     def test_delete_picli(self):
#         content_id = pd.read_csv("Data/test_add_picli.csv", delimiter=",").iloc[0, 2]
#         # 进入24小时feed版本页
#         self.driver.get(feed_url)
#         sleep(1)
#         # 搜索操作的消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
#         sleep(2)
#         # 删除消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).delete_data(content_id)
#         sleep(2)
#         # 获取页面数据结果
#         table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
#         data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status(content_id)
#         # 校验
#         assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
#         assert data_status == "后台删除"
#
#     def teardown(self):
#         self.driver.quit()


# 文字+视频
# class TestVideoHot24Feed():
#     def setup(self):
#         self.driver = webdriver.Chrome(options=chrome_options())
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#         login(self.driver)
#
#     @pytest.mark.parametrize(("content", "oid"), [videoli_data[0][:2]])
#     def test_add_videoli(self, content, oid):
#         # 进入"创建新消息-文字+视频"页
#         self.driver.get(page_url + page["文字+视频"])
#         sleep(1)
#         # 创建文字+视频消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).add_videoli(content, oid)
#         sleep(1)
#         # 进入24小时feed版本页
#         self.driver.get(feed_url)
#         sleep(300)
#         # 搜索新创建的消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).search_new_data(status["撤回"], feedtype["文字+视频"])
#         sleep(1)
#         # 将生成的新数据存到文件中以供后续使用
#         content_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_id()
#         data_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_id_attribute(content)
#         df = pd.read_csv("Data/test_add_videoli.csv", delimiter=",")
#         df['content_id'] = content_id
#         df['id'] = data_id
#         df.to_csv("Data/test_add_videoli.csv", index=False, encoding="utf-8")
#         # 获取页面数据结果
#         content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type(content_id)
#         table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
#         important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important(content_id)
#         # 校验
#         assert content_type == "文字+视频"
#         assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
#         assert important == "否"
#
#     def test_edit_videoli(self):
#         data_id = pd.read_csv("Data/test_add_videoli.csv", delimiter=",").iloc[0, 3]
#         content_id = pd.read_csv("Data/test_add_videoli.csv", delimiter=",").iloc[0, 2]
#         # 进入当前id编辑页
#         self.driver.get(page_url + page["文字+视频"] + "&id=" + str(data_id))
#         sleep(1)
#         # 编辑消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).edit_data()
#         sleep(1)
#         # 进入24小时feed版本页
#         self.driver.get(feed_url)
#         sleep(1)
#         # 搜索编辑的消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
#         sleep(3)
#         # 获取页面数据结果
#         table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
#         important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important(content_id)
#         # 校验
#         assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
#         assert important == "是"
#
#     def test_delete_videoli(self):
#         content_id = pd.read_csv("Data/test_add_videoli.csv", delimiter=",").iloc[0, 2]
#         # 进入24小时feed版本页
#         self.driver.get(feed_url)
#         sleep(1)
#         # 搜索操作的消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
#         sleep(2)
#         # 删除消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).delete_data(content_id)
#         sleep(2)
#         # 获取页面数据结果
#         table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
#         data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status(content_id)
#         # 校验
#         assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
#         assert data_status == "后台删除"
#
#     def teardown(self):
#         self.driver.quit()


# 文字+外链
# class TestLinkHot24Feed():
#     def setup(self):
#         self.driver = webdriver.Chrome(options=chrome_options())
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#         login(self.driver)
#
#     @pytest.mark.parametrize(("content", "oid"), [linkli_data[0][:2]])
#     def test_add_linkli(self, content, oid):
#         # 进入"创建新消息-文字+外链"页
#         self.driver.get(page_url + page["文字+外链"])
#         sleep(1)
#         # 创建文字+外链消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).add_linkli(content, oid)
#         sleep(1)
#         # # 进入24小时feed版本页
#         self.driver.get(feed_url)
#         sleep(2)
#         # 搜索新创建的消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).search_new_data(status["撤回"], feedtype["文字+外链"])
#         sleep(1)
#         # 将生成的新数据存到文件中以供后续使用
#         content_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_id()
#         data_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_id_attribute(content)
#         df = pd.read_csv("Data/test_add_linkli.csv", delimiter=",")
#         df['content_id'] = content_id
#         df['id'] = data_id
#         df.to_csv("Data/test_add_linkli.csv", index=False, encoding="utf-8")
#         # 获取页面数据结果
#         content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type(content_id)
#         table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
#         link_title = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_link_title(content_id)
#         important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important(content_id)
#         # 校验
#         assert content_type == "文字+外链"
#         assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
#         assert link_title == "国家移民管理局宣布：暂停！"
#         assert important == "否"
#
#     def test_edit_linkli(self):
#         data_id = pd.read_csv("Data/test_add_linkli.csv", delimiter=",").iloc[0, 3]
#         content_id = pd.read_csv("Data/test_add_linkli.csv", delimiter=",").iloc[0, 2]
#         # 进入当前id编辑页
#         self.driver.get(page_url + page["文字+外链"] + "&id=" + str(data_id))
#         sleep(2)
#         # 编辑消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).edit_link_data()
#         sleep(1)
#         # 进入24小时feed版本页
#         self.driver.get(feed_url)
#         sleep(1)
#         # 搜索编辑的消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
#         sleep(3)
#         # 获取页面数据结果
#         table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
#         important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important(content_id)
#         # 校验
#         assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
#         assert important == "是"
#
#     def test_delete_linkli(self):
#         content_id = pd.read_csv("Data/test_add_linkli.csv", delimiter=",").iloc[0, 2]
#         # 进入24小时feed版本页
#         self.driver.get(feed_url)
#         sleep(1)
#         # 搜索操作的消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
#         sleep(2)
#         # 删除消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).delete_data(content_id)
#         sleep(2)
#         # 获取页面数据结果
#         table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
#         data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status(content_id)
#         # 校验
#         assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
#         assert data_status == "后台删除"
#
#     def teardown(self):
#         self.driver.quit()


# 真人播报
# class TestListenHot24Feed():
#     def setup(self):
#         self.driver = webdriver.Chrome(options=chrome_options())
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#         login(self.driver)
#
#     @pytest.mark.parametrize(("oid", "content"), [listenli_data[0][:2]])
#     def test_add_listenli(self, oid, content):
#         # 进入"创建新消息-真人播报"页
#         self.driver.get(page_url + page["真人播报"])
#         sleep(1)
#         # 创建真人播报消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).add_listenli(oid, content)
#         sleep(1)
#         # 进入24小时feed版本页
#         self.driver.get(feed_url)
#         sleep(2)
#         # 搜索新创建的消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).search_new_data(status["撤回"], feedtype["真人播报"])
#         sleep(1)
#         # 将生成的新数据存到文件中以供后续使用
#         content_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_id()
#         data_id = hot_24_feed_page.Hot24FeedOper(self.driver).get_id_attribute(content)
#         df = pd.read_csv("Data/test_add_listenli.csv", delimiter=",")
#         df['content_id'] = content_id
#         df['id'] = data_id
#         df.to_csv("Data/test_add_listenli.csv", index=False, encoding="utf-8")
#         # 获取页面数据结果
#         content_type = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content_type(content_id)
#         table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
#         link_title = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_link_title(content_id)
#         important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important(content_id)
#         # 校验
#         assert content_type == "边看边听"
#         assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
#         assert link_title == "58万亿一夜蒸发，牵出韩国“史上最大诈骗犯”"
#         assert important == "否"
#
#     def test_edit_listenli(self):
#         data_id = pd.read_csv("Data/test_add_listenli.csv", delimiter=",").iloc[0, 3]
#         content_id = pd.read_csv("Data/test_add_listenli.csv", delimiter=",").iloc[0, 2]
#         # 进入当前id编辑页
#         self.driver.get(page_url + page["真人播报"] + "&id=" + str(data_id))
#         sleep(2)
#         # 编辑消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).edit_data()
#         sleep(1)
#         # 进入24小时feed版本页
#         self.driver.get(feed_url)
#         sleep(1)
#         # 搜索编辑的消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
#         sleep(3)
#         # 获取页面数据结果
#         table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
#         important = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_important(content_id)
#         # 校验
#         assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
#         assert important == "是"
#
#     def test_delete_linkli(self):
#         content_id = pd.read_csv("Data/test_add_listenli.csv", delimiter=",").iloc[0, 2]
#         # 进入24小时feed版本页
#         self.driver.get(feed_url)
#         sleep(1)
#         # 搜索操作的消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).search_data(str(content_id))
#         sleep(2)
#         # 删除消息
#         hot_24_feed_page.Hot24FeedScenarios(self.driver).delete_data(content_id)
#         sleep(2)
#         # 获取页面数据结果
#         table_content = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_content(content_id)
#         data_status = hot_24_feed_page.Hot24FeedOper(self.driver).get_table_status(content_id)
#         # 校验
#         assert table_content == "这是一条自动化测试用例，请审核老师通过就好"
#         assert data_status == "后台删除"
#
#     def teardown(self):
#         self.driver.quit()


if __name__ == "__main__":
    pytest.main(['-s', 'test_hot_24_feed.py::TestTextHot24Feed'])
