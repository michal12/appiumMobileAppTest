from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactListPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    ADD_CONTACT_BUTTON = (AppiumBy.ID, 'com.google.android.contacts:id/floating_action_button')
    EXIST_CONTACT = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="{contact_name}"]')
    SEARCH_CONTACT_FIELD = (AppiumBy.ID, 'com.google.android.contacts:id/open_search_bar_text_view')

    def click_add_contact_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_CONTACT_BUTTON)).click()

    def click_contact_by_name(self, contact_name):
        contact_elements = self.driver.find_elements(AppiumBy.ID, 'com.google.android.contacts:id/cliv_name_textview')
        print(contact_elements)
        for contact in contact_elements:
            if contact_name in contact.text:
                contact.click()
                return True

    def find_contact(self, contact_name):
        contact_elements = self.driver.find_elements(AppiumBy.ID, 'com.google.android.contacts:id/cliv_name_textview')
        return any(contact_name in contact.text for contact in contact_elements)

    def contact_exists(self, contact_name):
        sleep(3)
        if self.find_contact(contact_name):
            return True
