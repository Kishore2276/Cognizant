import { useState, useEffect } from "react";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

function App() {
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((response) => response.json())
      .then((data) => {
        const courseData = data.slice(0, 5).map((post, index) => ({
          id: post.id,
          name: post.title,
          code: `CS30${index + 1}`,
          credits: 4,
          grade: "A",
        }));

        setCourses(courseData);
        setLoading(false);
      })
      .catch(() => {
        setError("Failed to load courses.");
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    console.log("Courses updated");
  }, [courses]); // Runs only when courses state changes

  const handleEnroll = (course) => {
    if (!enrolledCourses.find((c) => c.id === course.id)) {
      setEnrolledCourses([...enrolledCourses, course]);
    }
  };

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  if (loading) {
    return <h2>Loading...</h2>;
  }

  if (error) {
    return <h2>{error}</h2>;
  }

  return (
    <>
      <Header
        siteName="Student Portal"
        enrolledCount={enrolledCourses.length}
      />

      <input
        type="text"
        placeholder="Search course..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />

      <div>
        {filteredCourses.map((course) => (
          <CourseCard
            key={course.id}
            {...course}
            onEnroll={handleEnroll}
          />
        ))}
      </div>

      <StudentProfile />

      <Footer />
    </>
  );
}

export default App;