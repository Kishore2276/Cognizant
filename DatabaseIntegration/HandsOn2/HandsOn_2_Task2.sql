use college_db;

ALTER TABLE students
ADD enrollment_year INT;

ALTER TABLE professors
ADD salary DECIMAL(10,2);

UPDATE students SET enrollment_year = 2022 WHERE student_id IN (1,2,3);
UPDATE students SET enrollment_year = 2023 WHERE student_id IN (4,5,6);
UPDATE students SET enrollment_year = 2024 WHERE student_id IN (7,8,9,10);

UPDATE professors SET salary = 85000 WHERE professor_id = 1;
UPDATE professors SET salary = 90000 WHERE professor_id = 2;
UPDATE professors SET salary = 95000 WHERE professor_id = 3;
UPDATE professors SET salary = 70000 WHERE professor_id = 4;
UPDATE professors SET salary = 100000 WHERE professor_id = 5;

SELECT *
FROM students
WHERE enrollment_year = 2022
ORDER BY student_name ASC;

SELECT *
FROM courses
WHERE credits > 3
ORDER BY credits DESC;

SELECT *
FROM professors
WHERE salary BETWEEN 80000 AND 95000;

SELECT *
FROM students
WHERE email LIKE '%@college.edu';

SELECT enrollment_year,
COUNT(*) AS total_students
FROM students
GROUP BY enrollment_year;

