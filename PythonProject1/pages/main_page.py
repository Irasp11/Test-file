from .base_page import BasePage
from selenium.webdriver.common.by import By

from .locators import LoginPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(LoginPageLocators.LOGIN_LINK)
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)