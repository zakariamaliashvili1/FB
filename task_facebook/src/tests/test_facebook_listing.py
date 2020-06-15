# Test Case
# Candidate needs to use: Chrome, selenium, python on ubuntu linux instance on EC2(Free instance).
# Login to FB and go to marketplace and create a listing (it can be for anything you like)
# Then delete the listing
from src.all_imports import *
import src.steps.utilities as utils
import pytest

logger = utils.create_logger()
data = utils.yaml_loader(f"{utils.ROOT_DIR}/data/configs.yaml")


@pytest.mark.testlisting
def test_list_item(browser):

    item_title = 'Iphone X brand new'
    pricee = '1000$'
    photo_xpath = f"{utils.ROOT_DIR}/data/uploads/iphonex.png"
    delete_reason = "No, haven't sold"
    marketplace = Marketplace(browser)

    logger.info("# Open browser and navigate to Facebook marketplace")
    marketplace.click_marketplace()
    marketplace.click_create_new_list()
    marketplace.click_item_forsale()

    logger.info('filling out the form...')
    marketplace.add_photo(photo_xpath)
    time.sleep(5)
    marketplace.enter_title(item_title)
    marketplace.enter_price(pricee)
    marketplace.select_category()
    marketplace.select_condition()
    marketplace.take_screenshot()
    marketplace.click_next()
    time.sleep(3)
    marketplace.publish()
    time.sleep(5)
    marketplace.take_screenshot()
    logger.info('item published')
    sleep(5)

    marketplace.delete_listing(item_title)
    # marketplace.confirm_delete(delete_reason)
    marketplace.take_screenshot()

    logger.info('test completed!')
