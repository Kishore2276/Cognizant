# Hands-On 3 – Test Automation Process, Lifecycle & Framework Types

## Task 1: Automation Decision and Test Case Selection

---

## 17. Criteria for Deciding Whether a Test Case Should Be Automated

### 1. Repetitive Test Cases

Tests that are executed repeatedly are ideal for automation because they save time and effort.

**Application to the Scenario:**

The `POST /api/courses` endpoint is tested after every code change, making it a good candidate for automation.

---

### 2. Regression Testing

Regression tests verify that existing functionality continues to work after changes.

**Application to the Scenario:**

Automating the `POST /api/courses` test ensures that course creation continues to work after every update.

---

### 3. Stable Functionality

Features that rarely change are suitable for automation because maintenance effort is low.

**Application to the Scenario:**

The API endpoint for course creation is a stable feature, making it suitable for automation.

---

### 4. High-Risk Functionality

Critical business functions should always be automated to reduce production risks.

**Application to the Scenario:**

Creating a course is a core feature of the Course Management API. Failure of this feature directly impacts users.

---

### 5. Data-Driven Testing

Tests requiring multiple input combinations are ideal for automation.

**Application to the Scenario:**

The API can be tested using various valid and invalid course details without manually repeating the same process.

---

## 18. Automation vs Manual Testing

| Test Case | Decision | Justification |
|-----------|----------|---------------|
| a) Regression test for all CRUD endpoints after every code change | **Automate** | Executed frequently and suitable for regression testing. |
| b) Exploratory testing of a new search feature | **Manual** | Requires human creativity and exploration. |
| c) Performance test with 100 concurrent users | **Automate** | Performance testing requires automation tools to simulate multiple users. |
| d) UI test for the login form | **Automate** | Login is a stable and frequently tested feature. |
| e) Verify the Swagger API documentation is accurate | **Manual** | Documentation review requires human verification. |
| f) Smoke test to verify the API is reachable after deployment | **Automate** | Smoke tests are executed after every deployment and should run automatically. |

---

## 19. Test Automation ROI

### Definition

Test Automation ROI (Return on Investment) measures whether the time and cost spent creating automated tests are recovered through repeated execution.

### Given

- Automation development time = **4 hours**
- Manual execution time = **30 minutes (0.5 hours)**

### ROI Calculation

Each automated execution saves:

```
0.5 hours
```

Runs required to recover automation effort:

```
4 ÷ 0.5 = 8 runs
```

After the **10th run**, a **20% maintenance overhead** is added.

Maintenance time per run:

```
20% × 0.5 = 0.1 hour
```

Net saving after maintenance:

```
0.5 − 0.1 = 0.4 hour per run
```

### Conclusion

- Automation pays for itself after approximately **8 test runs**.
- After the 10th run, maintenance slightly reduces the time savings, but automation remains significantly more efficient than manual testing.

---

## 20. Flaky Test

### Definition

A flaky test is a test that sometimes **passes and sometimes fails** without any changes to the application's code.

### Example

A Selenium test clicks the **Login** button before the page has fully loaded.

- Sometimes the test passes.
- Sometimes it fails because the element is not yet available.

### Strategies to Prevent Flaky Tests

1. Use **Explicit Waits** instead of fixed delays (`Thread.sleep()`).

2. Use stable and unique locators such as **ID** or **Name** instead of dynamic XPath expressions.

3. Ensure test independence by resetting test data before each execution.

---

# Conclusion

This hands-on explains how to identify suitable candidates for automation, differentiate between manual and automated testing, calculate automation ROI, and understand flaky tests along with techniques to improve test reliability.


---

# Task 2 – Compare Automation Framework Types

## 21. Comparison of Automation Framework Types

### 1. Linear Framework

**Description:**

The Linear Framework is the simplest automation framework where test scripts are written and executed sequentially without reusable components. It is suitable for small projects with simple test cases.

**Advantage:**

- Easy to understand and implement.

**Disadvantage:**

- Difficult to maintain as the project grows.

**Example:**

Automating a single course creation workflow in the Course Management System.

---

### 2. Modular Framework

**Description:**

The Modular Framework divides the application into independent modules. Separate test scripts are created for each module and reused whenever needed.

**Advantage:**

- High code reusability.

**Disadvantage:**

- Initial framework setup requires more effort.

**Example:**

Separate modules for Login, Course Management, Student Management, and Logout.

---

### 3. Data-Driven Framework

**Description:**

The Data-Driven Framework stores test data outside the test scripts (Excel, CSV, JSON, etc.), allowing the same script to execute with multiple input values.

**Advantage:**

- Supports testing with multiple datasets without changing the code.

**Disadvantage:**

- Test data management can become complex.

**Example:**

Testing login functionality using 50 different username and password combinations.

---

### 4. Keyword-Driven Framework

**Description:**

The Keyword-Driven Framework executes tests based on predefined keywords such as Click, EnterText, Login, and Verify. Test cases are created using these keywords.

**Advantage:**

- Non-technical team members can design test cases.

**Disadvantage:**

- Framework implementation is more complex.

**Example:**

Creating login test cases using keywords like **OpenBrowser**, **EnterUsername**, **EnterPassword**, and **ClickLogin**.

---

### 5. Hybrid Framework

**Description:**

The Hybrid Framework combines the features of Modular, Data-Driven, and Keyword-Driven frameworks to provide maximum flexibility, maintainability, and scalability.

**Advantage:**

- Highly reusable, scalable, and suitable for large automation projects.

**Disadvantage:**

- Requires experienced team members to design and maintain.

**Example:**

A Course Management automation suite that uses reusable page objects, external test data, and keyword-based execution.

---

## 22. Recommended Framework for the Given Scenario

### Recommended Framework

**Hybrid Framework (Modular + Data-Driven + Keyword-Driven)**

### Justification

The Hybrid Framework is the best choice because:

- It supports testing login with **50 different user credentials** using the Data-Driven approach.
- Login functionality can be reused across **20 test cases** using the Modular approach.
- Non-technical team members can create test cases using predefined keywords in the Keyword-Driven approach.
- The framework is scalable, maintainable, and suitable for large Selenium automation projects.

---

## 23. Hybrid Framework Folder Structure

```text
CourseManagementAutomation
│
├── config
│   └── config.properties
│
├── testdata
│   ├── LoginData.xlsx
│   └── CourseData.xlsx
│
├── pages
│   ├── LoginPage.java
│   ├── CoursePage.java
│   └── DashboardPage.java
│
├── tests
│   ├── LoginTest.java
│   ├── CourseTest.java
│   └── SmokeTest.java
│
├── utilities
│   ├── ExcelUtils.java
│   ├── DriverFactory.java
│   ├── WaitUtils.java
│   └── ScreenshotUtils.java
│
├── reports
│
└── pom.xml
```

### Folder Description

| Folder | Purpose |
|---------|----------|
| config | Stores application configuration files. |
| testdata | Stores Excel, CSV, or JSON files used for Data-Driven testing. |
| pages | Contains Page Object Model (POM) classes for each application page. |
| tests | Contains Selenium test scripts. |
| utilities | Stores reusable helper classes such as WebDriver setup, waits, screenshots, and Excel handling. |
| reports | Stores generated automation execution reports. |
| pom.xml | Manages Maven dependencies and project configuration. |

---

# Conclusion

This hands-on compares the five major automation framework types, recommends the most suitable framework for a real-world Selenium project, and presents a well-organized Hybrid Framework folder structure. The Hybrid Framework is the preferred choice for enterprise automation because it combines reusability, flexibility, maintainability, and support for data-driven testing.