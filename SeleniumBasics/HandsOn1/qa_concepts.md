# Hands-On 1 – QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Map Testing Types to a Real System

---

## 1. Test Levels

### Unit Testing

**Description:**

Test a single function that validates course details before saving them.

**Example Test Case:**

- Verify that the function rejects an empty course name.

**Expected Result:**

- Validation error is displayed.
- The course is not saved.

**Testing Type:**

- Functional Testing

---

### Integration Testing

**Description:**

Test the communication between the Course Management API and the database.

**Example Test Case:**

- Send a **POST** request to create a new course.
- Verify that the course information is stored correctly in the database.

**Expected Result:**

- API returns **HTTP 201 (Created)**.
- The course record is successfully inserted into the database.

**Testing Type:**

- Functional Testing

---

### System Testing

**Description:**

Test the complete end-to-end course creation process.

**Example Test Case:**

1. User submits course details.
2. API validates the input.
3. Database stores the course information.
4. API returns a success response.

**Expected Result:**

- The course is created successfully and displayed in the application.

**Testing Type:**

- Functional Testing

---

### User Acceptance Testing (UAT)

**Description:**

A college administrator creates a new course using the application.

**Expected Result:**

- The administrator confirms that the application satisfies the business requirements and works as expected.

**Testing Type:**

- Functional Testing

---

## 2. Functional vs Non-Functional Testing

### Functional Testing

Functional Testing verifies whether the application performs the required functions correctly.

**Examples:**

- Create a course
- Update a course
- Delete a course
- Retrieve course details

---

### Non-Functional Testing

Non-Functional Testing evaluates how well the application performs in terms of speed, reliability, scalability, and security.

**Example: Performance Testing**

- Send **1000 simultaneous API requests**.
- Verify that the average response time is **less than 2 seconds**.
- Ensure no request failures occur.

---

## 3. Black-Box Testing vs White-Box Testing

### Black-Box Testing

- Tester does not know the internal source code.
- Testing is based only on inputs and expected outputs.
- Focuses on application functionality.
- Commonly performed by **QA Testers**.

### White-Box Testing

- Tester has knowledge of the application's source code.
- Tests internal logic, conditions, loops, and code paths.
- Focuses on code quality and implementation.
- Commonly performed by **Developers**.

---

## 4. Formal Test Cases for `POST /api/courses`

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|--------------|------------|-----------------|---------------|-----------|
| TC001 | Create a course with valid details | API is running | Send a POST request with valid course details | HTTP 201 Created and the course is saved successfully | | |
| TC002 | Create a course without a course name | API is running | Send a POST request with an empty course name | HTTP 400 Bad Request with a validation error | | |
| TC003 | Create a duplicate course | Course already exists | Send a POST request with the same course details | Duplicate course is rejected with an appropriate error message | | |

---

---

# Task 2 – Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

### Defect Lifecycle Flow

```text
New
 ↓
Assigned
 ↓
Open
 ↓
Fixed
 ↓
Retest
 ↓
Verified
 ↓
Closed
```

### Explanation of Each State

| State | Description |
|--------|-------------|
| New | The tester identifies and reports a new defect. |
| Assigned | The defect is assigned to a developer for fixing. |
| Open | The developer starts analysing and working on the defect. |
| Fixed | The developer fixes the defect and marks it as fixed. |
| Retest | The QA tester retests the application to verify the fix. |
| Verified | The tester confirms that the defect has been fixed successfully. |
| Closed | The defect is closed because it has been resolved successfully. |

### Additional Paths

#### Rejected

A defect is marked as **Rejected** when:

- It is not actually a defect.
- The issue cannot be reproduced.
- The reported behaviour is expected.

#### Deferred

A defect is marked as **Deferred** when:

- The fix is postponed.
- It has low business impact.
- It will be fixed in a future release.

---

## 6. Severity and Priority Classification

| Bug | Severity | Priority | Justification |
|-----|----------|----------|---------------|
| a) POST /api/courses returns 500 Internal Server Error for all requests | **Critical** | **P1** | The application cannot create courses, affecting all users. |
| b) Course names longer than 150 characters are silently truncated | **Medium** | **P3** | Data is modified incorrectly but the application still works. |
| c) Swagger API documentation contains a typo | **Low** | **P4** | Cosmetic issue that does not affect functionality. |
| d) Login occasionally returns HTTP 401 on the first attempt | **High** | **P2** | Login sometimes fails, affecting user experience and indicating instability. |

---

## 7. Defect Report

| Field | Details |
|--------|---------|
| Defect ID | BUG-001 |
| Title | POST /api/courses returns HTTP 500 Internal Server Error |
| Environment | Windows 11, Chrome Browser, Local Development |
| Build Version | v1.0 |
| Severity | Critical |
| Priority | P1 |
| Steps to Reproduce | 1. Start the application.<br>2. Open Postman.<br>3. Send a POST request to `/api/courses` with valid course details.<br>4. Observe the response. |
| Expected Result | Course should be created successfully with HTTP 201 Created. |
| Actual Result | API returns HTTP 500 Internal Server Error and the course is not created. |
| Attachments | Screenshot of HTTP 500 Error |

---

## 8. Difference Between Severity and Priority

### Severity

Severity indicates **how serious the defect is** and how much it impacts the application's functionality.

### Priority

Priority indicates **how urgently the defect should be fixed**.

### Example

Suppose the company CEO notices that the company logo on the login page is displayed incorrectly.

- **Severity:** Low (the application works normally)
- **Priority:** High (the company wants it fixed immediately before a client demonstration)

This example shows that a defect can have **Low Severity but High Priority**.

---

# Conclusion

This hands-on explains the complete software testing process, including testing levels, defect lifecycle, severity and priority classification, defect reporting, and different testing techniques used in Quality Assurance.