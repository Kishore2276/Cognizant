from selenium.webdriver.common.by import By
import time
from pages.checkbox_page import CheckboxPage


def test_checkbox(driver, base_url):

    driver.get(base_url)

    driver.find_element(By.LINK_TEXT, "Checkbox Demo").click()

    print(driver.current_url)
    time.sleep(10)   # Keep the browser open for 10 seconds

    page = CheckboxPage(driver)

    page.check_option()