from selenium.webdriver.common.by import By
from .base_page import BasePage


class InputFormPage(BasePage):

    PAGE_URL = "https://www.lambdatest.com/selenium-playground/input-form-demo"

    NAME = (By.ID, "name")
    EMAIL = (By.ID, "inputEmail4")
    PASSWORD = (By.ID, "inputPassword4")
    COMPANY = (By.ID, "company")
    WEBSITE = (By.ID, "websitename")
    COUNTRY = (By.NAME, "country")
    CITY = (By.ID, "inputCity")
    ADDRESS1 = (By.ID, "inputAddress1")
    ADDRESS2 = (By.ID, "inputAddress2")
    STATE = (By.ID, "inputState")
    ZIP = (By.ID, "inputZip")

    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//p[contains(text(),'Thanks for contacting us')]"
    )

    def open(self):
        self.navigate_to(self.PAGE_URL)

    def fill_form(
        self,
        name,
        email,
        password,
        company,
        website,
        city,
        address1,
        address2,
        state,
        zip_code,
    ):

        self.wait_for_element(self.NAME).send_keys(name)
        self.wait_for_element(self.EMAIL).send_keys(email)
        self.wait_for_element(self.PASSWORD).send_keys(password)
        self.wait_for_element(self.COMPANY).send_keys(company)
        self.wait_for_element(self.WEBSITE).send_keys(website)
        self.wait_for_element(self.CITY).send_keys(city)
        self.wait_for_element(self.ADDRESS1).send_keys(address1)
        self.wait_for_element(self.ADDRESS2).send_keys(address2)
        self.wait_for_element(self.STATE).send_keys(state)
        self.wait_for_element(self.ZIP).send_keys(zip_code)

    def submit_form(self):
        self.wait_for_element(self.SUBMIT_BUTTON).click()

    def get_success_message(self):
        return self.wait_for_element(self.SUCCESS_MESSAGE).text