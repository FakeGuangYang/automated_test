from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from Test.PageObject import login_page
from Common.parse_csv import parse_csv

data = parse_csv("Data/test_001_login.csv")
url = "https://sso.sohu-inc.com/login?" \
      "service=http://opt.mrd.sohuno.com:10020/operation/ssoValidate?returnUrl=/jina/news/index"
chrome_webdriver_path = "chromedriver"
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('blink-settings=imagesEnabled=false')


@pytest.mark.parametrize(("username", "password", "status"), data)
class TestLogin():
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=chrome_webdriver_path, chrome_options=chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)

    def test_001_login(self, username, password, status):
        login_page.LoginScenarios(self.driver).login(username, password)
        if status == '0':
            text = login_page.LoginOper(self.driver).get_login_failed_info()
            assert text == '登录失败！请输入有效的用户名/密码。'
        elif status == '1':
            text = login_page.LoginOper(self.driver).get_login_name()
            assert text == 'guangyang219579@sohu-inc.com'
        else:
            print("Wrong status.")

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(['-s', 'test_001_login.py'])
