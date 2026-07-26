from flask import Flask, request
import requests

app = Flask(__name__)

COURSE_SERVICE = "http://127.0.0.1:5001"
STUDENT_SERVICE = "http://127.0.0.1:5002"


@app.route("/api/courses", methods=["GET"])
def gateway_courses():

    response = requests.get(
        f"{COURSE_SERVICE}/courses"
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


@app.route("/api/students", methods=["GET"])
def gateway_students():

    response = requests.get(
        f"{STUDENT_SERVICE}/students"
    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


@app.route("/api/students/<int:student_id>/enroll", methods=["POST"])
def gateway_enroll(student_id):

    response = requests.post(

        f"{STUDENT_SERVICE}/students/{student_id}/enroll",

        json=request.json

    )

    return (
        response.content,
        response.status_code,
        response.headers.items()
    )


if __name__=="__main__":
    app.run(port=5000,debug=True)