USE college_db;

-- ==========================================
-- Task 2: Add Indexes and Compare Plans
-- ==========================================

-- Create an index on enrollment_year
CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

-- Create a composite UNIQUE index
CREATE UNIQUE INDEX idx_enrollments_student_course
ON enrollments(student_id, course_id);

-- Create an index on course_name
CREATE INDEX idx_courses_course_name
ON courses(course_name);

-- Run EXPLAIN again after creating indexes

EXPLAIN
SELECT s.student_name,
       c.course_name
FROM enrollments e
JOIN students s
ON s.student_id = e.student_id
JOIN courses c
ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

/*
Comparison with Baseline:

Before Index:
- students table used Access Type = ALL
- Full Table Scan occurred on students
- Rows examined = 10

After Index:
- students table uses the index
  idx_students_enrollment_year
- Access Type changes from ALL to ref/range
- Fewer rows are examined
- Query performance improves

The composite UNIQUE index on
(student_id, course_id)
prevents duplicate enrollments.

The index on course_name improves
search performance for course-related queries.
*/

-- Expected Observation:
-- Access Type for students should improve.
-- The query should examine fewer rows.
-- Query execution becomes faster.