from src.all_imports import *
import src.steps.utilities as utils


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.logger = utils.create_logger()

    def click_element_by_xpath(self, xpath):
        try:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.click()
        except NoSuchElementException:
            self.take_screenshot('error')
            self.logger.error(f"element was not found {xpath}")
            raise

    def enter_text_by_xpath(self, xpath, phrase):
        try:
            element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.clear()
            element.send_keys(phrase)
        except NoSuchElementException:
            self.take_screenshot('error')
            self.logger.error(f"element was not found {xpath}")
            raise

    def take_screenshot(self, phrase=""):
        filepath = f"{utils.ROOT_DIR}/screenshots/{phrase}{utils.get_timestamp()}.png"
        self.driver.save_screenshot(filepath)
        self.logger.info(f"screenshot is taken :{filepath}")
