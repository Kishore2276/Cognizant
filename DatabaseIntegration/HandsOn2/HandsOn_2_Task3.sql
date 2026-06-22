SELECT s.student_name,
       d.dept_name
FROM students s
INNER JOIN departments d
ON s.dept_id = d.dept_id;

SELECT e.enrollment_id,
       s.student_name,
       c.course_name,
       e.grade
FROM enrollments e
INNER JOIN students s
ON e.student_id = s.student_id
INNER JOIN courses c
ON e.course_id = c.course_id;

SELECT s.student_id,
       s.student_name
FROM students s
LEFT JOIN enrollments e
ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

SELECT c.course_id,
       c.course_name,
       COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_name;

SELECT d.dept_name,
       p.professor_name,
       p.salary
FROM departments d
LEFT JOIN professors p
ON d.dept_id = p.dept_id;

