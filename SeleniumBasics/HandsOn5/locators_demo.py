"""
Hands-On 5 - Locator Strategies

This program demonstrates:
1. ID Locator
2. Name Locator
3. Class Name Locator
4. Tag Name Locator
5. XPath (Absolute)
6. XPath (Relative)
7. CSS Selectors
8. XPath text()
9. XPath contains()

Ranking of Locator Strategies (Best → Worst)

1. ID
2. Name
3. CSS Selector
4. Relative XPath
5. Class Name
6. Absolute XPath

Reason:
- ID is unique and most reliable.
- Name is stable in many forms.
- CSS Selectors are fast and readable.
- Relative XPath is flexible.
- Class Name may not be unique.
- Absolute XPath is fragile because HTML structure changes easily.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/")

driver.implicitly_wait(10)

# -------------------------------------------------
# Step 32 - Simple Form Demo
# -------------------------------------------------

driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

print("Opened Simple Form Demo")

# Locate the message input field

element_id = driver.find_element(By.ID, "user-message")
print("ID Locator : PASS")

element_name = driver.find_element(By.NAME, "user-message")
print("Name Locator : PASS")

element_class = driver.find_element(By.CLASS_NAME, "form-control")
print("Class Locator : PASS")

element_tag = driver.find_element(By.TAG_NAME, "input")
print("Tag Locator : PASS")

# Absolute XPath
element_abs = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/section[2]/div/div/div[1]/div/div[2]/form/div/input"
)
print("Absolute XPath : PASS")

# Relative XPath
element_rel = driver.find_element(
    By.XPATH,
    "//input[@id='user-message']"
)
print("Relative XPath : PASS")

# -------------------------------------------------
# Step 33 - CSS Selectors
# -------------------------------------------------

driver.find_element(By.CSS_SELECTOR, "#user-message")
print("CSS by ID : PASS")

driver.find_element(By.CSS_SELECTOR, "[name='user-message']")
print("CSS by Attribute : PASS")

driver.find_element(By.CSS_SELECTOR, "form div input")
print("CSS Parent > Child : PASS")

# -------------------------------------------------
# Step 34 - Checkbox Demo
# -------------------------------------------------

driver.back()

driver.find_element(By.LINK_TEXT, "Checkbox Demo").click()

option1 = driver.find_element(
    By.XPATH,
    "//label[text()='Option 1']"
)

print("XPath text() : PASS")

options = driver.find_elements(
    By.XPATH,
    "//label[contains(text(),'Option')]"
)

print("XPath contains() found", len(options), "elements")

# -------------------------------------------------

print("\nAll locator strategies executed successfully.")

driver.quit()