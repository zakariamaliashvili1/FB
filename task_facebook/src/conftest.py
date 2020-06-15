import pytest
from selenium import webdriver
from src.all_imports import *
import src.steps.utilities as utils


logger = utils.create_logger()
data = utils.yaml_loader(f"{utils.ROOT_DIR}/data/configs.yaml")

URL = data['home_url']
EMAIL = data['email']
PASSWORD = data['pasword']


@pytest.fixture(scope="session")
def browser():
    # step: 1  - SETUP (before your scope)
    # driver = webdriver.Chrome(chrome_url)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    logger.info('browser is opened...')
    
    login(driver, URL, EMAIL, PASSWORD)

    yield driver
    # TEARDOWN (after your scope)
    # step: 6 - closing the browser
    # driver.quit()
