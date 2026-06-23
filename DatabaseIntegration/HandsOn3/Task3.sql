USE college_db;

DELIMITER $$

CREATE PROCEDURE sp_enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN

    DECLARE enroll_count INT;

    SELECT COUNT(*)
    INTO enroll_count
    FROM enrollments
    WHERE student_id = p_student_id
    AND course_id = p_course_id;

    IF enroll_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Student is already enrolled in this course';
    ELSE
        INSERT INTO enrollments(student_id, course_id, enrollment_date)
        VALUES(p_student_id, p_course_id, p_enrollment_date);
    END IF;

END $$

DELIMITER ;

CALL sp_enroll_student(1,2,'2026-06-22');
SELECT * FROM enrollments;