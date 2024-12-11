import React, { useState, useEffect } from "react";
import axios from "axios";

const CourseList = () => {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    fetchCourses();
  }, []);

  const fetchCourses = async () => {
    try {
      const response = await axios.get("http://localhost:8000/api/courses/");
      setCourses(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const deleteCourse = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/api/courses/${id}/`);
      fetchCourses();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="mt-4">
      <h2>Lista de Cursos</h2>
      <button className="btn btn-primary mb-3">Crear Curso</button>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Créditos</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {courses.map((course) => (
            <tr key={course.id}>
              <td>{course.name}</td>
              <td>{course.credits}</td>
              <td>
                <button className="btn btn-warning btn-sm">Editar</button>
                <button
                  className="btn btn-danger btn-sm ms-2"
                  onClick={() => deleteCourse(course.id)}
                >
                  Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CourseList;

