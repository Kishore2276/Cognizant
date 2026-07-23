import { useState } from "react";

function StudentProfile() {
  const [profile, setProfile] = useState({
    name: "",
    email: "",
    semester: "",
  });

  const handleChange = (e) => {
    setProfile({
      ...profile,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <div
      style={{
        border: "1px solid gray",
        borderRadius: "8px",
        padding: "20px",
        marginTop: "20px",
        width: "350px",
      }}
    >
      <h2>Student Profile</h2>

      <input
        type="text"
        name="name"
        placeholder="Name"
        value={profile.name}
        onChange={handleChange}
      />

      <br /><br />

      <input
        type="email"
        name="email"
        placeholder="Email"
        value={profile.email}
        onChange={handleChange}
      />

      <br /><br />

      <input
        type="text"
        name="semester"
        placeholder="Semester"
        value={profile.semester}
        onChange={handleChange}
      />

      <hr />

      <p><strong>Name:</strong> {profile.name}</p>
      <p><strong>Email:</strong> {profile.email}</p>
      <p><strong>Semester:</strong> {profile.semester}</p>
    </div>
  );
}

export default StudentProfile;