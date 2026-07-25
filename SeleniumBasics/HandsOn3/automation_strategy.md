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