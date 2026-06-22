SELECT c.course_name,
       COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY c.course_name;

SELECT d.dept_name,
       ROUND(AVG(p.salary), 2) AS average_salary
FROM departments d
LEFT JOIN professors p
ON d.dept_id = p.dept_id
GROUP BY d.dept_name;

SELECT d.dept_name,
       SUM(p.salary) AS total_budget
FROM departments d
JOIN professors p
ON d.dept_id = p.dept_id
GROUP BY d.dept_name
HAVING SUM(p.salary) > 600000;

SELECT grade,
       COUNT(*) AS grade_count
FROM enrollments
WHERE course_id = 1
GROUP BY grade;

SELECT d.dept_name,
       COUNT(e.student_id) AS total_students
FROM departments d
JOIN courses c
ON d.dept_id = c.dept_id
JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY d.dept_name
HAVING COUNT(e.student_id) > 2;

