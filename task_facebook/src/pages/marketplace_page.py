import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import src.steps.utilities as utils
from src.pages.base_page import BasePage

logger = utils.create_logger()


class Marketplace(BasePage):
    # LOCATORS
    marketplace_button = "//div[contains(text(),'Marketplace')]"
    create_new_listing_link = "//span[contains(text(),'Create New Listing')]"
    item_forsale_link = "//a[@href='/marketplace/create/item/']"
    title_input = "//span[text()='Title']/../input"
    price_input = "//span[text()='Price']/../input"
    categories_list = "//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/label/div/div/div/img[1]"
    categories_phone_option = "//span[contains(text(),'Mobile Phones')]"
    condition_list = "//div[5]//div[1]//div[1]//label[1]//div[1]//div[1]//div[1]//div[1]"
    condition_new_option = "//span[text()='New']"
    next_button = "//span[text()='Next']"
    publish_button = "//span[contains(text(),'Publish')]"
    more_button = "//div[@aria-label='More' and @role='button']"
    delete_button = "//span[text()='Delete Listing']"
    dialog_delete_button = "/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div/div[1]/div[1]/div[1]/div/span"
    dialog_next_button = "//div[@aria-label='Delete Listing']//span[text()='Next']"
    add_photo_input = "//input[@accept='image/*,image/heif,image/heic']"

    # ACTIONS ON THE PAGE
    def click_marketplace(self):
        self.click_element_by_xpath(self.marketplace_button)

    def click_create_new_list(self):
        self.click_element_by_xpath(self.create_new_listing_link)

    def click_item_forsale(self):
        self.click_element_by_xpath(self.item_forsale_link)

    def enter_title(self, phrase):
        self.enter_text_by_xpath(self.title_input, phrase)

    def enter_price(self, phrase):
        self.enter_text_by_xpath(self.price_input, phrase)

    def select_category(self):
        self.click_element_by_xpath(self.categories_list)
        time.sleep(1)
        self.click_element_by_xpath(self.categories_phone_option)

    def select_condition(self):
        self.click_element_by_xpath(self.condition_list)
        self.click_element_by_xpath(self.condition_new_option)

    def click_next(self):
        self.click_element_by_xpath(self.next_button)

    def publish(self):
        self.click_element_by_xpath(self.publish_button)

    def delete_listing(self, item_title):
        logger.info(f"Deleting the item {item_title}")
        listed_xpath = f"//div[@data-pagelet='MainFeed']//span[text()='{item_title}']"
        self.wait.until(EC.presence_of_element_located((By.XPATH, listed_xpath)))
        self.click_element_by_xpath(self.more_button)
        time.sleep(5)
        self.click_element_by_xpath(self.delete_button)
        logger.info('listing deleted.')
        time.sleep(3)
        self.click_element_by_xpath(self.dialog_delete_button)


    # def confirm_delete(self):
        # dialog_reason_xpath = f"""//div[@aria-label='Delete Listing']//span[text()="{reason}"]"""
        # logger.info(f"confirming with reason : {reason}")
        # self.click_element_by_xpath(self.dialog_delete_button)
        # time.sleep(1)
        # self.click_element_by_xpath(dialog_reason_xpath)
        # time.sleep(1)
        # self.click_element_by_xpath(self.dialog_next_button)
        logger.info(f"deleting is confirmed.")


    def add_photo(self, filepath):
        logger.info(f"adding a photo : {filepath}")
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, self.add_photo_input)))
        element.send_keys(filepath)
        logger.info(f"photo uploaded!")


    @property
    def get_title(self):
        return self.driver.title


class PopUpWindow(BasePage):
    openwindow_button = "//button[@id='openwindow']"
    search_box = "//input[@id='search-courses']"

    def click_openwindow(self):
        self.click_element_by_xpath(self.openwindow_button)

    def search_text(self, text):
        element = self.driver.find_element_by_xpath(self.search_box)
        element.clear()
        element.send_keys(text)
        element.submit()
