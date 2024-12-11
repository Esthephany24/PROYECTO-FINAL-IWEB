import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import ProfessorList from "./components/ProfessorList";
import CourseList from "./components/CourseList";
import CourseLoadForm from "./components/CourseLoadForm";

const App = () => {
  return (
    <Router>
      <div className="container">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
          <Link className="navbar-brand" to="/">Gestión Académica</Link>
          <div className="navbar-nav">
            <Link className="nav-link" to="/professors">Listar Profesores</Link>
            <Link className="nav-link" to="/courses">Listar Cursos</Link>
            <Link className="nav-link" to="/course-load">Carga Académica</Link>
          </div>
        </nav>

        <Routes>
          <Route
            path="/"
            element={
              <div className="text-center mt-5">
                <h1>Bienvenido a la Gestión Académica</h1>
                <p>Organiza la carga académica de manera eficiente</p>
                <img
                  src="/images/academic_management.jpg" // Ruta de la imagen
                  alt="Gestión Académica"
                  className="img-fluid"
                  style={{ maxWidth: "60%", borderRadius: "10px", marginTop: "20px" }}
                />
              </div>
            }
          />
          <Route path="/professors" element={<ProfessorList />} />
          <Route path="/courses" element={<CourseList />} />
          <Route path="/course-load" element={<CourseLoadForm />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;

