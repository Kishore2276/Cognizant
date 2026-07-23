function CourseCard(props) {
  return (
    <div
      style={{
        border: "1px solid gray",
        borderRadius: "8px",
        padding: "15px",
        margin: "20px 0",
        width: "300px",
        backgroundColor: "#ffffff"
      }}
    >
      <h2>{props.name}</h2>

      <p><strong>Code:</strong> {props.code}</p>

      <p><strong>Credits:</strong> {props.credits}</p>

      <p><strong>Grade:</strong> {props.grade}</p>
    </div>
  );
}

export default CourseCard;