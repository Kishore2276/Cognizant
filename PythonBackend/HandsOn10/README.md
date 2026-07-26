# Microservices Decomposition

## Course Service

Responsibility:
- Manage courses

Endpoints:
- GET /courses
- GET /courses/{id}
- POST /courses

Database:
- courses.db

---

## Student Service

Responsibility:
- Manage students

Endpoints:
- GET /students
- GET /students/{id}
- POST /students

Database:
- students.db

---

## Auth Service (Concept)

Responsibility:
- Registration
- Login
- JWT Validation

Database:
- users.db

---

## Notification Service (Concept)

Responsibility:
- Email notifications

Database:
- notifications.db