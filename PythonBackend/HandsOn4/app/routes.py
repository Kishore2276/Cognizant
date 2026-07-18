from flask import Blueprint, request, jsonify

main = Blueprint("main", __name__)

courses = [
    {"id": 1, "name": "Python", "code": "PY101", "credits": 3},
    {"id": 2, "name": "Flask", "code": "FL201", "credits": 4}
]

def make_response_json(data, status_code):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code


# GET /
@main.route("/")
def home():
    return jsonify({"message": "Course API is running"})


# POST /
@main.route("/", methods=["POST"])
def create_course():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    required = ["name", "code", "credits"]

    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    new_course = {
        "id": len(courses) + 1,
        "name": data["name"],
        "code": data["code"],
        "credits": data["credits"]
    }

    courses.append(new_course)

    return make_response_json(new_course, 201)


# GET /<id>
@main.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            return make_response_json(course, 200)

    return jsonify({"error": "Course not found"}), 404


# PUT /<id>
@main.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    data = request.get_json()

    for course in courses:
        if course["id"] == course_id:
            course["name"] = data.get("name", course["name"])
            course["code"] = data.get("code", course["code"])
            course["credits"] = data.get("credits", course["credits"])

            return make_response_json(course, 200)

    return jsonify({"error": "Course not found"}), 404


# DELETE /<id>
@main.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)
            return jsonify({"message": "Course deleted"}), 200

    return jsonify({"error": "Course not found"}), 404