Hands-On 1 – QA Concepts, Functional Testing & Defect Lifecycle
Task 1: Map Testing Types to a Real System
1. Test Levels
Unit Testing

Description

Test the function that validates course details before saving.

Example Test Case

Verify that the function rejects an empty course name.
Expected Result:
Validation error is displayed and the course is not saved.

Type

Functional Testing

Integration Testing

Description

Test communication between the Course API and the database.

Example Test Case

Send a POST request to create a course.
Verify that the course is stored in the database.

Expected Result

API returns HTTP 201 and the record is inserted successfully.

Type

Functional Testing

System Testing

Description

Test the complete course creation process.

Example Test Case

User submits course details.
API validates data.
Database stores the record.
API returns success response.

Expected Result

The course is successfully created and displayed.

Type

Functional Testing

User Acceptance Testing (UAT)

Description

A college administrator creates a new course using the application.

Expected Result

The admin confirms that the system behaves according to business requirements.

Type

Functional Testing

2. Functional vs Non-Functional Testing
Functional Testing

Checks whether the application performs the required functionality correctly.

Example:

Create a course
Update a course
Delete a course
Retrieve course details
Non-Functional Testing

Checks how well the application performs.

Example:

Performance Testing

Send 1000 API requests simultaneously and verify that the average response time is less than 2 seconds without failures.

3. Black-Box vs White-Box Testing
Black-Box Testing
Tester does not know the internal source code.
Tests are based only on inputs and outputs.
Usually performed by QA Testers.
White-Box Testing
Tester knows the internal code.
Tests methods, loops, conditions and logic.
Usually performed by Developers.
4. Formal Test Cases for POST /api/courses
Test Case ID	Description	Preconditions	Test Steps	Expected Result	Actual Result	Pass/Fail
TC001	Create a course with valid details	API is running	Send POST request with valid course data	HTTP 201 Created and course saved		
TC002	Create a course without course name	API is running	Send POST request with empty course name	Validation error (HTTP 400)		
TC003	Create duplicate course	Course already exists	Send POST request with same course details	Duplicate record is rejected