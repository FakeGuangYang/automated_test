from selenium.webdriver.common.by import By


# Login page objects
class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_username(self):
        # find and return username element
        ele = self.driver.find_element(By.ID, 'userName')
        return ele

    def find_password(self):
        # find and return password element
        ele = self.driver.find_element(By.ID, 'pass')
        return ele

    def find_login_button(self):
        # find and return login button element
        ele = self.driver.find_element(By.ID, 'loginBtn')
        return ele

    def find_login_name(self):
        # find and return login name element
        ele = self.driver.find_element(By.XPATH, '//div[@class="info-container"]/div[@class="name"]')
        return ele

    def find_login_failed_info(self):
        # find and return login failed info element
        ele = self.driver.find_element(By.ID, 'myError')
        return ele


# Login page operations
class LoginOper(object):
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def input_username(self, username):
        self.login_page.find_username().clear()
        self.login_page.find_username().send_keys(username)

    def input_password(self, password):
        self.login_page.find_password().clear()
        self.login_page.find_password().send_keys(password)

    def click_login_button(self):
        self.login_page.find_login_button().click()

    def get_login_name(self):
        return self.login_page.find_login_name().text

    def get_login_failed_info(self):
        return self.login_page.find_login_failed_info().text


# Login page scenarios
class LoginScenarios(object):
    def __init__(self, driver):
        self.login_oper = LoginOper(driver)

    def login(self, username, password):
        self.login_oper.input_username(username)
        self.login_oper.input_password(password)
        self.login_oper.click_login_button()
