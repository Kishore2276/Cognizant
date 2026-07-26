from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest


# -------------------------------
# Test 1
# -------------------------------
@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "Selenium Automation",
        "12345"
    ]
)
def test_simple_form_submission(driver, base_url, message):

    # Your code...


# -------------------------------
# Test 2
# -------------------------------
def test_checkbox_demo(driver, base_url):

    # Your code...


# -------------------------------
# Test 3
# -------------------------------
def test_dropdown_selection(driver, base_url):

    driver.get(base_url)

    driver.find_element(By.LINK_TEXT, "Select Dropdown List").click()

    dropdown = Select(
        driver.find_element(By.ID, "select-demo")
    )

    dropdown.select_by_visible_text("Wednesday")

    assert dropdown.first_selected_option.text == "Wednesday"