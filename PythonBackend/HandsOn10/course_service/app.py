from flask import Flask, jsonify, request

app = Flask(__name__)

courses = {
    1: {
        "id": 1,
        "name": "Python",
        "code": "CS101"
    }
}

@app.route("/")
def home():
    return jsonify({
        "service": "Course Service"
    })

@app.route("/courses", methods=["GET"])
def get_courses():
    return jsonify(list(courses.values()))

@app.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):

    if course_id not in courses:
        return jsonify({"error": "Course not found"}),404

    return jsonify(courses[course_id])

@app.route("/courses", methods=["POST"])
def create_course():

    data=request.json

    new_id=len(courses)+1

    courses[new_id]={
        "id":new_id,
        "name":data["name"],
        "code":data["code"]
    }

    return jsonify(courses[new_id]),201

if __name__=="__main__":
    app.run(port=5001,debug=True)