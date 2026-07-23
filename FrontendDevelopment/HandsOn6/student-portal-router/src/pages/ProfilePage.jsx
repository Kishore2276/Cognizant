import { useSelector, useDispatch } from "react-redux";

import { unenroll } from "../redux/enrollmentSlice";

function ProfilePage() {

  const dispatch = useDispatch();

  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <div>
      <h2>Student Profile</h2>

      <h3>Enrolled Courses</h3>

      {enrolledCourses.length === 0 ? (
        <p>No courses enrolled.</p>
      ) : (
        enrolledCourses.map((course) => (
          <div
            key={course.id}
            style={{
              border: "1px solid gray",
              padding: "10px",
              margin: "10px 0",
            }}
          >
            <h4>{course.name}</h4>

            <button
              onClick={() =>
                dispatch(unenroll(course.id))
              }
            >
              Remove
            </button>
          </div>
        ))
      )}
    </div>
  );
}

export default ProfilePage;