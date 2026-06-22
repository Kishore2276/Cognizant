USE college_db;

ALTER TABLE students
ADD phone_number VARCHAR(15);

ALTER TABLE courses
ADD max_seats INT DEFAULT 60;

ALTER TABLE enrollments
ADD grade CHAR(1);

ALTER TABLE enrollments
ADD CONSTRAINT check_grade
CHECK (grade IN ('A', 'B', 'C', 'D', 'E') OR grade IS NULL);

ALTER TABLE departments
ADD hod_name VARCHAR(100);

ALTER TABLE departments
CHANGE hod_name head_of_dept VARCHAR(100);

ALTER TABLE students
DROP COLUMN phone_number;

DESC departments;
DESC students;
DESC courses;
DESC professors;
DESC enrollments;
