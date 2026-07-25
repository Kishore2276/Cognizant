"""
Hands-On 5
Task 2 - WebDriverWait and Expected Conditions
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

wait = WebDriverWait(driver,10)

driver.get("https://www.lambdatest.com/selenium-playground/")

# ---------------------------------------------------
# Step 36
# ---------------------------------------------------

driver.find_element(By.LINK_TEXT,"Bootstrap Alerts").click()

wait.until(
    EC.element_to_be_clickable(
        (By.ID,"autoclosable-btn-success")
    )
).click()

alert = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,".alert-success")
    )
)

assert "successfully" in alert.text.lower()

print("Step 36 Passed")

# ---------------------------------------------------
# Step 37
# ---------------------------------------------------

driver.refresh()

start = time.time()

driver.find_element(By.ID,"autoclosable-btn-success").click()

time.sleep(3)

sleep_time = time.time()-start

print("Using sleep():",round(sleep_time,2),"seconds")

driver.refresh()

start = time.time()

wait.until(
    EC.element_to_be_clickable(
        (By.ID,"autoclosable-btn-success")
    )
).click()

wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR,".alert-success")
    )
)

wait_time = time.time()-start

print("Using Explicit Wait:",round(wait_time,2),"seconds")

# Explicit waits are preferred because they wait only
# until the required condition becomes true.
# sleep() always waits the full duration even if the
# element is already available.

# ---------------------------------------------------
# Step 38
# ---------------------------------------------------

driver.refresh()

button = wait.until(
    EC.element_to_be_clickable(
        (By.ID,"autoclosable-btn-success")
    )
)

button.click()

print("Step 38 Passed")

# visibility_of_element_located()
# -> Element is visible.

# element_to_be_clickable()
# -> Element is visible, enabled,
#    and ready for clicking.

# ---------------------------------------------------
# Step 39
# ---------------------------------------------------

driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

fluent_wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

row = fluent_wait.until(
    EC.visibility_of_element_located(
        (By.XPATH,"//table/tbody/tr[1]")
    )
)

print("Fluent Wait Successful")

print("Row Text:")
print(row.text)

driver.quit()