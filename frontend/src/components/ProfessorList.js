import React, { useState, useEffect } from "react";
import axios from "axios";

const ProfessorList = () => {
  const [professors, setProfessors] = useState([]);

  useEffect(() => {
    fetchProfessors();
  }, []);

  const fetchProfessors = async () => {
    try {
      const response = await axios.get("http://localhost:8000/api/professors/");
      setProfessors(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const deleteProfessor = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/api/professors/${id}/`);
      fetchProfessors();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="mt-4">
      <h2>Lista de Profesores</h2>
      <button className="btn btn-success mb-3">Agregar Profesor</button>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Departamento</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {professors.map((professor) => (
            <tr key={professor.id}>
              <td>{professor.name}</td>
              <td>{professor.department}</td>
              <td>
                <button className="btn btn-warning btn-sm">Editar</button>
                <button
                  className="btn btn-danger btn-sm ms-2"
                  onClick={() => deleteProfessor(professor.id)}
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

export default ProfessorList;

