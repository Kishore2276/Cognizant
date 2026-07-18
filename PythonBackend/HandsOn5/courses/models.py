from app import db

class Department(db.Model):
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(100), unique=True, nullable=False)

    courses = db.relationship("Course", back_populates="department")


class Course(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id")
    )

    department = db.relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = db.relationship(
        "Enrollment",
        back_populates="course"
    )


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)

    enrollments = db.relationship(
        "Enrollment",
        back_populates="student"
    )


class Enrollment(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id")
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id")
    )

    student = db.relationship(
        "Student",
        back_populates="enrollments"
    )

    course = db.relationship(
        "Course",
        back_populates="enrollments"
    )