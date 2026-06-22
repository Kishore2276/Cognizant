use college_db;
INSERT INTO departments (dept_name) 
VALUES
('Computer Science'),
('Mechanical'),
('Civil'),
('Electrical'),
('Electronics');

INSERT INTO students (student_name, email, dept_id)
VALUES
('Kishore', 'kishore@gmail.com', 1),
('Rahul', 'rahul@gmail.com', 1),
('Priya', 'priya@gmail.com', 2),
('Arjun', 'arjun@gmail.com', 3),
('Meena', 'meena@gmail.com', 1),
('Suresh', 'suresh@gmail.com', 4),
('Anitha', 'anitha@gmail.com', 5),
('Vijay', 'vijay@gmail.com', 2);

INSERT INTO courses (course_name, credits, dept_id)
VALUES
('DBMS', 4, 1),
('Java Programming', 3, 1),
('Thermodynamics', 4, 2),
('Structural Engineering', 3, 3),
('Circuit Theory', 4, 4);

INSERT INTO professors (professor_name, email, dept_id)
VALUES
('Dr Kumar', 'kumar@college.com', 1),
('Dr Ravi', 'ravi@college.com', 2),
('Dr Priya', 'priya@college.com', 3),
('Dr Suresh', 'suresh@college.com', 4),
('Dr Meena', 'meena@college.com', 5);

INSERT INTO enrollments
(student_id, course_id, enrollment_date, grade)
VALUES
(1,1,'2026-06-01','A'),
(2,1,'2026-06-01','B'),
(3,3,'2026-06-02','C'),
(4,4,'2026-06-03',NULL),
(5,1,'2026-06-04','C'),
(6,5,'2026-06-05',NULL),
(7,2,'2026-06-06','A'),
(8,3,'2026-06-07','B');

INSERT INTO students (student_name, email, dept_id)
VALUES
('Karan', 'karan@gmail.com', 1),
('Divya', 'divya@gmail.com', 2);

UPDATE enrollments
SET grade = 'B'
WHERE student_id = 5
AND course_id = 1;

SELECT *
FROM enrollments
WHERE student_id = 5
AND course_id = 1;

SELECT *
FROM enrollments
WHERE grade IS NULL;

DELETE FROM enrollments
WHERE grade IS NULL;

SELECT COUNT(*) AS Total_Students
FROM students;

SELECT COUNT(*) AS Total_Enrollments
FROM enrollments;

SELECT * FROM students;

SELECT * FROM enrollments;