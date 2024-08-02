from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


class CreateContactPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    NAME_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[@text="First name"]')
    PHONE_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[@text="Phone"]')
    SAVE_BUTTON = (AppiumBy.ID, 'com.google.android.contacts:id/toolbar_button')

    def set_first_name(self, name):
        self.wait.until(EC.element_to_be_clickable(self.NAME_FIELD)).send_keys(name)

    def set_phone(self, phone):
        self.wait.until(EC.element_to_be_clickable(self.PHONE_FIELD)).send_keys(phone)

    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    # only for demo
    def fill_contact_data(self, name, phone):
        self.set_first_name(name)
        self.set_phone(phone)

