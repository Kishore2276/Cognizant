USE college_db;

-- ==========================================
-- Task 1: Baseline Performance — No Indexes
-- ==========================================

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
EXPLAIN Analysis

Table: students (alias s)
Access Type: ALL
Key Used: NULL
Rows Examined: 10
Extra: Using where

Table: enrollments (alias e)
Access Type: ref
Key Used: student_id
Rows Examined: 2
Extra: Using where

Table: courses (alias c)
Access Type: eq_ref
Key Used: PRIMARY
Rows Examined: 1

Observations:
1. The students table performs a Full Table Scan
   because no index exists on enrollment_year.

2. MySQL examines approximately 10 rows
   in the students table.

3. The enrollments table uses the student_id
   foreign key for joining.

4. The courses table uses its PRIMARY KEY
   for efficient lookup.

5. Since the dataset is small, query performance
   is acceptable. However, as the number of rows
   increases, Full Table Scans may slow down
   query execution.
*/

-- Yes. A Full Table Scan occurs on the students table (type = ALL).

-- Estimated Rows Examined:
-- students     = 10
-- enrollments  = 2
-- courses      = 1

-- Query cost is low because the dataset is small.
-- Performance can be improved by creating indexes.