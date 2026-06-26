from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from DatabaseIntegration.HandsOn7.models import Enrollment

engine = create_engine(
    "mysql+mysqlconnector://root:220706@localhost/college_db_orm",
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()



print("\n===== N+1 QUERY =====")

enrollments = session.query(Enrollment).all()

for enrollment in enrollments:
    print(
        enrollment.student.student_name,
        "-",
        enrollment.course.course_name
    )



print("\n===== OPTIMIZED QUERY USING joinedload =====")

enrollments = session.query(Enrollment).options(
    joinedload(Enrollment.student),
    joinedload(Enrollment.course)
).all()

for enrollment in enrollments:
    print(
        enrollment.student.student_name,
        "-",
        enrollment.course.course_name
    )

session.close()