from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckboxPage(BasePage):

    PAGE_URL = "https://www.lambdatest.com/selenium-playground/checkbox-demo"

    SINGLE_CHECKBOX = (
        By.ID,
        "isAgeSelected"
    )

    def open(self):
    self.navigate_to(self.PAGE_URL)

    def check_option(self):
        checkbox = self.wait_for_element(self.SINGLE_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_option(self):
        checkbox = self.wait_for_element(self.SINGLE_CHECKBOX)
        if checkbox.is_selected():
            checkbox.click()

    def is_option_checked(self):
        return self.wait_for_element(
            self.SINGLE_CHECKBOX
        ).is_selected()