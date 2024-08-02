import json
import os
import unittest

from time import sleep

from appium import webdriver
from appium.options.common import AppiumOptions

from pages.contact_create_page import CreateContactPage
from pages.contact_detail_page import ContactDetailPage
from pages.contact_list_page import ContactListPage

TEST_CONTACT_NAME = "Test_Contact"
TEST_CONTACT_PHONE = "1234567890"
APPIUM_SERVER_URL = 'http://localhost:4723'

config_path = os.path.join(os.path.dirname(__file__),'..', 'config', 'config.json')

with open(config_path) as config_file:
    capabilities = json.load(config_file)


class ContactApplicationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Remote(APPIUM_SERVER_URL, options=AppiumOptions.load_capabilities(
            AppiumOptions(), capabilities))
        self.contact_list_page = ContactListPage(self.driver)
        self.create_contact_page = CreateContactPage(self.driver)
        self.contact_detail_page = ContactDetailPage(self.driver)

    def test_add_contact(self) -> None:
        sleep(3)
        self.contact_list_page.click_add_contact_button()
        self.create_contact_page.fill_contact_data(TEST_CONTACT_NAME, TEST_CONTACT_PHONE)
        self.create_contact_page.click_save_button()
        self.contact_detail_page.verify_contact_detail_page(TEST_CONTACT_NAME)
        self.contact_detail_page.click_navigate_up()
        exists = self.contact_list_page.contact_exists(TEST_CONTACT_NAME)
        assert exists

    def test_delete_contact(self) -> None:
        sleep(3)
        self.contact_list_page.click_contact_by_name(TEST_CONTACT_NAME)
        self.contact_detail_page.close_pop_up_window()
        self.contact_detail_page.open_more_action_menu()
        self.contact_detail_page.click_delete_option()
        self.contact_detail_page.click_confirm_delete()
        exists = self.contact_list_page.contact_exists(TEST_CONTACT_NAME)
        assert not exists

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
