import { createContext, useState } from "react";

export const EnrollmentContext = createContext();

export function EnrollmentProvider({ children }) {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const enrollCourse = (course) => {
    if (!enrolledCourses.find((c) => c.id === course.id)) {
      setEnrolledCourses([...enrolledCourses, course]);
    }
  };

  const removeCourse = (id) => {
    setEnrolledCourses(
      enrolledCourses.filter((course) => course.id !== id)
    );
  };

  return (
    <EnrollmentContext.Provider
      value={{
        enrolledCourses,
        enrollCourse,
        removeCourse,
      }}
    >
      {children}
    </EnrollmentContext.Provider>
  );
}