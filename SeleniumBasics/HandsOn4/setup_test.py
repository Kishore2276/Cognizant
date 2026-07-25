"""
Hands-On 4 – Selenium WebDriver Setup, Browser Drivers & Basic Commands

Selenium Components

1. WebDriver
   - WebDriver automates browser actions by communicating with browser drivers.

2. Selenium Grid
   - Selenium Grid enables parallel execution on multiple browsers and machines.

3. Selenium IDE
   - Selenium IDE is a record-and-playback browser extension for creating basic automation scripts.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome Options
options = webdriver.ChromeOptions()

# Run browser in headless mode
options.add_argument("--headless=new")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Implicit wait
driver.implicitly_wait(10)

# -------------------------
# Task 1
# -------------------------

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Page Title:", driver.title)

# -------------------------
# Task 2
# -------------------------

# Step 28
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

assert "simple-form-demo" in driver.current_url

print("Current URL:", driver.current_url)

driver.back()

# Step 29
driver.execute_script("window.open('https://www.google.com');")

print("Open Windows:", driver.window_handles)

driver.switch_to.window(driver.window_handles[1])

print("Google Title:", driver.title)

# Step 30
driver.switch_to.window(driver.window_handles[0])

driver.save_screenshot("playground_screenshot.png")

print("Screenshot saved successfully.")

# Step 31

# Set browser window size
driver.set_window_size(1280, 800)

# Get current window size
size = driver.get_window_size()

print("Window Size:", size)

# Consistent browser size ensures that responsive web pages
# render the same layout during every automation execution.

driver.quit()