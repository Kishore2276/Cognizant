import { useNavigate } from "react-router-dom";

import { useDispatch } from "react-redux";

import { enroll } from "../redux/enrollmentSlice";

import courses from "../data/courses";

function CoursesPage() {

  const navigate = useNavigate();

  const dispatch = useDispatch();

  return (
    <div>
      <h2>Courses</h2>

      {courses.map((course) => (
        <div
          key={course.id}
          style={{
            border: "1px solid gray",
            padding: "15px",
            margin: "10px",
            width: "300px",
            borderRadius: "8px",
          }}
        >
          <h3>{course.name}</h3>

          <p>{course.code}</p>

          <button
            onClick={() =>
              navigate(`/courses/${course.id}`)
            }
          >
            View Details
          </button>

          {" "}

          <button
            onClick={() => {
              dispatch(enroll(course));
              navigate("/profile");
            }}
          >
            Enroll
          </button>
        </div>
      ))}
    </div>
  );
}

export default CoursesPage;