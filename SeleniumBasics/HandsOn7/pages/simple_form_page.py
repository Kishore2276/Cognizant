from selenium.webdriver.common.by import By
from .base_page import BasePage



class SimpleFormPage(BasePage):

    
    PAGE_URL = "https://www.lambdatest.com/selenium-playground/simple-form-demo"

    MESSAGE_INPUT = (By.ID, "user-message")
    SHOW_MESSAGE_BUTTON = (By.ID, "showInput")
    DISPLAY_MESSAGE = (By.ID, "message")

    def open(self):
        self.navigate_to(self.PAGE_URL)

    def enter_message(self, text):
        element = self.wait_for_element(self.MESSAGE_INPUT)
        element.clear()
        element.send_keys(text)

    def click_submit(self):
        self.wait_for_element(self.SHOW_MESSAGE_BUTTON).click()

    def get_displayed_message(self):
        return self.wait_for_element(self.DISPLAY_MESSAGE).text