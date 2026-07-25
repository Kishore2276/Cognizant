# Hands-On 2 – SDLC vs TDLC: V-Model & Agile QA Integration

## Task 1: V-Model Mapping

---

## 9. V-Model Diagram

```
                 SDLC (Development)                 TDLC (Testing)

Requirements -----------------------------> Acceptance Testing
      |                                            ^
      |                                            |
System Design ---------------------------> System Testing
      |                                            ^
      |                                            |
Architecture Design ---------------------> Integration Testing
      |                                            ^
      |                                            |
Module Design ---------------------------> Unit Testing
      |                                            ^
      |                                            |
                 \                              /
                  \                            /
                   \                          /
                      ------ Coding ------
```

### Explanation

The V-Model shows that every development phase has a corresponding testing phase. Testing activities are planned early during development and executed after coding is completed.

---

## 10. SDLC to TDLC Mapping

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|------------|--------------------------|------------------------|
| Requirements | Acceptance Testing | Acceptance Test Plan |
| System Design | System Testing | System Test Cases |
| Architecture Design | Integration Testing | Integration Test Cases |
| Module Design | Unit Testing | Unit Test Cases |
| Coding | Execution of All Tests | Source Code |

---

## 11. Entry and Exit Criteria

### Unit Testing

**Entry Criteria**

- Module development completed.
- Source code available.
- Unit test cases prepared.

**Exit Criteria**

- All unit test cases executed.
- Critical defects fixed.
- Code coverage achieved.

---

### Integration Testing

**Entry Criteria**

- Unit testing completed successfully.
- Integrated modules available.
- Integration test cases prepared.

**Exit Criteria**

- Interfaces validated.
- No critical integration defects.
- Test cases passed.

---

### System Testing

**Entry Criteria**

- Complete application deployed.
- System test cases prepared.
- Test environment ready.

**Exit Criteria**

- Functional testing completed.
- No critical or high-severity defects.
- Test summary report completed.

---

### User Acceptance Testing (UAT)

**Entry Criteria**

- System testing completed.
- Business users available.
- UAT environment ready.

**Exit Criteria**

- Business requirements satisfied.
- User approval received.
- Product ready for deployment.

---

## 12. QA Engagement in the V-Model

### 1. Requirements Review

QA participates during the Requirements phase by reviewing business requirements to identify missing, unclear, or conflicting requirements before development begins.

### 2. System Design Review

QA reviews the system design to understand the application's workflow and prepares test cases early, ensuring better test coverage and fewer defects later.

---

# Conclusion

The V-Model establishes a direct relationship between every SDLC phase and its corresponding testing phase. Early QA involvement improves software quality, reduces development cost, and helps identify defects before implementation.

---

# Task 2 – Agile QA and Shift-Left Testing

## 13. Problems in Traditional Waterfall Testing

In the Waterfall model, testing begins only after the entire development phase is completed. This creates the following problems for the Course Management API project:

### Problem 1: Late Defect Detection

Defects are identified only after development is complete, making them more expensive and time-consuming to fix.

### Problem 2: Requirement Misunderstanding

If developers misunderstand a requirement, the mistake may remain unnoticed until the testing phase, resulting in rework and project delays.

### Problem 3: Delayed Product Delivery

Fixing defects at the end of the project delays testing, increases development cost, and postpones product release.

---

## 14. QA Role in Agile Ceremonies

| Agile Ceremony | QA Engineer Responsibilities |
|----------------|------------------------------|
| Sprint Planning | Reviews user stories, defines acceptance criteria, estimates testing effort, and identifies potential risks. |
| Daily Standup | Shares testing progress, reports blockers, discusses defects, and coordinates with developers. |
| Sprint Review | Verifies completed features, performs demo testing, and confirms that acceptance criteria are met. |
| Retrospective | Discusses issues faced during the sprint and suggests improvements to the testing process. |

---

## 15. Shift-Left Testing Practices

### 1. Review Requirements for Testability

QA reviews requirements early to identify missing or unclear requirements before development begins.

### 2. Write Test Cases Before Coding (TDD/BDD)

QA prepares test cases before implementation so developers clearly understand expected behaviour.

### 3. Static Code Analysis

Developers use static analysis tools to detect coding issues, security vulnerabilities, and code quality problems before execution.

### 4. API Contract Testing Before Integration

QA verifies that API request and response formats match the agreed contract before integrating with other modules.

---

## 16. Acceptance Criteria (Given-When-Then)

### Scenario 1 – Successful Course Creation

**Given**
- The college administrator is logged into the application.
- Valid course details are entered.

**When**
- The administrator clicks the **Create Course** button.

**Then**
- The course is created successfully.
- A success message is displayed.
- The course appears in the course list.

---

### Scenario 2 – Duplicate Course Code

**Given**
- A course with the same course code already exists.

**When**
- The administrator attempts to create another course using the same course code.

**Then**
- The course is not created.
- An error message stating **"Course code already exists"** is displayed.

---

### Scenario 3 – Missing Required Fields

**Given**
- The administrator leaves one or more mandatory fields empty.

**When**
- The administrator clicks the **Create Course** button.

**Then**
- Validation messages are displayed for the missing fields.
- The course is not created until all required fields are completed.

---

# Conclusion

This hands-on demonstrates the relationship between SDLC and TDLC through the V-Model, explains QA responsibilities in Agile development, introduces the Shift-Left testing approach, and shows how acceptance criteria can be written using the Given-When-Then format to ensure software quality from the early stages of development.