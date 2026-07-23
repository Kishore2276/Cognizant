function Header(props) {
  return (
    <header>
      <h1>{props.siteName}</h1>

      <nav>
        <a href="#">Home</a> |{" "}
        <a href="#">Courses</a> |{" "}
        <a href="#">Profile</a>
      </nav>

      <p>
        <strong>Enrolled Courses:</strong> {props.enrolledCount}
      </p>

      <hr />
    </header>
  );
}

export default Header;