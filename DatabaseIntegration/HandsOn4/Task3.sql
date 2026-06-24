# Task 3: Identify and Fix the N+1 Problem

import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5907cse@123",
    database="college_db"
)

cursor = conn.cursor(dictionary=True)

print("========== N+1 QUERY VERSION ==========")

start_time = time.time()

query_count = 1

# First query
cursor.execute("SELECT * FROM enrollments")
enrollments = cursor.fetchall()

# N additional queries
for enrollment in enrollments:

    cursor.execute(
        "SELECT student_name FROM students WHERE student_id = %s",
        (enrollment['student_id'],)
    )

    student = cursor.fetchone()

    print(
        f"Enrollment ID: {enrollment['enrollment_id']} | "
        f"Student: {student['student_name']}"
    )

    query_count += 1

end_time = time.time()

print("\nQueries Executed:", query_count)
print("Execution Time:", round(end_time - start_time, 6), "seconds")

print("\n========== OPTIMIZED JOIN VERSION ==========")

start_time = time.time()

query_count = 1

cursor.execute("""
SELECT e.enrollment_id,
       s.student_name
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
""")

results = cursor.fetchall()

for row in results:
    print(
        f"Enrollment ID: {row['enrollment_id']} | "
        f"Student: {row['student_name']}"
    )

end_time = time.time()

print("\nQueries Executed:", query_count)
print("Execution Time:", round(end_time - start_time, 6), "seconds")

cursor.close()
conn.close()

print("\n========== ANALYSIS ==========")
print("N+1 Version executes 1 query for enrollments")
print("and N additional queries for each student.")
print("JOIN Version executes only 1 query.")
print("For 10,000 enrollments:")
print("N+1 Version = 10,001 queries")
print("JOIN Version = 1 query")

             OUTPUT
========== N+1 QUERY VERSION ==========
Enrollment ID: 1 | Student: Kishore
Enrollment ID: 2 | Student: Rahul
Enrollment ID: 3 | Student: Priya
...

Queries Executed: 11
Execution Time: 0.005321 seconds

========== OPTIMIZED JOIN VERSION ==========
Enrollment ID: 1 | Student: Kishore
Enrollment ID: 2 | Student: Rahul
Enrollment ID: 3 | Student: Priya
...

Queries Executed: 1
Execution Time: 0.001102 seconds

========== ANALYSIS ==========
N+1 Version executes 1 query for enrollments
and N additional queries for each student.
JOIN Version executes only 1 query.
For 10,000 enrollments:
N+1 Version = 10,001 queries
JOIN Version = 1 query