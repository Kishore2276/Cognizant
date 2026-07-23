function Header(props) {
  return (
    <header>
      <h1>{props.siteName}</h1>

      <nav>
        <a href="#">Home</a> |{" "}
        <a href="#">Courses</a> |{" "}
        <a href="#">Profile</a>
      </nav>

      <hr />
    </header>
  );
}

export default Header;