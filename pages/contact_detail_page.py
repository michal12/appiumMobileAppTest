from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactDetailPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    MORE_OPTIONS_ICON = (AppiumBy.ID, 'com.google.android.contacts:id/action_bar_overflow_menu')
    DELETE_CONTACT_OPTION = (AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.google.android.contacts:id/title" and @text="Delete"]')
    CONFIRM_DELETE_BUTTON = (AppiumBy.ID, 'android:id/button1')
    NAVIGATE_UP = (AppiumBy.ACCESSIBILITY_ID, 'Navigate up')
    CONTACT_TITLE_NAME = (AppiumBy.ID, 'com.google.android.contacts:id/large_title')
    CLOSE_POP_UP = (AppiumBy.ID, 'android:id/closeButton')

    def open_more_action_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.MORE_OPTIONS_ICON)).click()

    def click_delete_option(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_CONTACT_OPTION)).click()

    def click_confirm_delete(self):
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BUTTON)).click()

    def close_pop_up_window(self):
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_POP_UP)).click()

    def click_navigate_up(self):
        self.wait.until(EC.element_to_be_clickable(self.NAVIGATE_UP)).click()

    def verify_contact_detail_page(self, expected_title):
        self.close_pop_up_window()
        contact_title_element = self.wait.until(EC.visibility_of_element_located(self.CONTACT_TITLE_NAME))
        assert contact_title_element.text == expected_title
