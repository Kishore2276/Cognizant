from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import declarative_base, relationship


engine = create_engine(
    "mysql+mysqlconnector://root:220706@localhost/college_db_orm"
)

Base = declarative_base()


class Department(Base):
    __tablename__ = 'departments'

    dept_id = Column(Integer, primary_key=True, autoincrement=True)
    dept_name = Column(String(100), nullable=False, unique=True)

    students = relationship("Student", back_populates="department")
    courses = relationship("Course", back_populates="department")
    professors = relationship("Professor", back_populates="department")



class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    dept_id = Column(Integer, ForeignKey('departments.dept_id'))

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")



class Course(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(100), nullable=False)
    credits = Column(Integer, nullable=False)

    dept_id = Column(Integer, ForeignKey('departments.dept_id'))

    department = relationship("Department", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")



class Professor(Base):
    __tablename__ = 'professors'

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    professor_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    dept_id = Column(Integer, ForeignKey('departments.dept_id'))

    department = relationship("Department", back_populates="professors")



class Enrollment(Base):
    __tablename__ = 'enrollments'

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)

    student_id = Column(Integer, ForeignKey('students.student_id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))

    enrollment_date = Column(Date)

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")



Base.metadata.create_all(engine)

print("All tables created successfully in college_db_orm")