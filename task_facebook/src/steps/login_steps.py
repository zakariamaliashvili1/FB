from src.all_imports import *
import src.steps.utilities as utils

logger = utils.create_logger()


def login(driver, url, email, password):

    driver.get(url)

    login_page = Login(driver)
    logger.info("loggin page started..")
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_login()
    logger.info('logged in successfully!')
