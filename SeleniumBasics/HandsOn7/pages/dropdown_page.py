from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class DropdownPage(BasePage):

    PAGE_URL = "https://www.lambdatest.com/selenium-playground/select-dropdown-demo"

    DAY_DROPDOWN = (By.ID, "select-demo")

    def open(self):
        self.navigate_to(self.PAGE_URL)

    def get_selected_day(self):
        dropdown = Select(
        self.wait_for_element(self.DAY_DROPDOWN)
    )
    return dropdown.first_selected_option.text

    def select_day(self, day_name):
        dropdown = Select(
            self.wait_for_element(self.DAY_DROPDOWN)
        )
        dropdown.select_by_visible_text(day_name)