from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

students = {
    1: {
        "id":1,
        "name":"John"
    }
}

@app.route("/")
def home():
    return jsonify({
        "service":"Student Service"
    })

@app.route("/students",methods=["GET"])
def get_students():

    return jsonify(list(students.values()))

@app.route("/students/<int:student_id>",methods=["GET"])
def get_student(student_id):

    if student_id not in students:

        return jsonify({
            "error":"Student not found"
        }),404

    return jsonify(students[student_id])

@app.route("/students",methods=["POST"])
def create_student():

    data=request.json

    new_id=len(students)+1

    students[new_id]={
        "id":new_id,
        "name":data["name"]
    }

    return jsonify(students[new_id]),201

@app.route("/students/<int:student_id>/enroll", methods=["POST"])
def enroll_student(student_id):

    if student_id not in students:
        return jsonify({
            "error": "Student not found"
        }),404

    data = request.json

    course_id = data["course_id"]

    try:

        response = requests.get(
            f"http://127.0.0.1:5001/courses/{course_id}"
        )

    except requests.exceptions.ConnectionError:

        return jsonify({
            "error":"Course Service unavailable"
        }),503

    if response.status_code != 200:

        return jsonify({
            "error":"Course does not exist"
        }),404

    return jsonify({

        "message":"Enrollment Successful",

        "student":student_id,

        "course":course_id

    }),200

if __name__=="__main__":
    app.run(port=5002,debug=True)