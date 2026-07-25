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

# Conclusion

This hands-on demonstrates the different software testing levels, functional and non-functional testing, the differences between Black-Box and White-Box testing, and the process of writing formal test cases for a Course Management API.