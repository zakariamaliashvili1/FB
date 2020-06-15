from src.all_imports import *
from src.pages.base_page import BasePage
import src.steps.utilities as utils

logger = utils.create_logger()


class Login(BasePage):
    # LOCATORS
    login_email = "//input[@name='email']"
    login_password = "//input[@name='pass']"
    login_button = "//html//body//div//div//div//div//div//div//div//form//table//tbody//tr//td//label//input"

    # ACTIONS ON THE PAGE
    def enter_email(self, uname):
        self.enter_text_by_xpath(self.login_email, uname)

    def enter_password(self, phrase):
        self.enter_text_by_xpath(self.login_password, phrase)

    def click_login(self):
        self.click_element_by_xpath(self.login_button)
