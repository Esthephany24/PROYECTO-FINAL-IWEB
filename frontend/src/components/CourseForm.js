import React, { useState } from "react";
import axios from "axios";

const CourseForm = ({ course = {}, onSuccess }) => {
  const [name, setName] = useState(course.name || "");
  const [credits, setCredits] = useState(course.credits || "");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (course.id) {
        await axios.put(`http://localhost:8000/api/courses/${course.id}/`, { name, credits }, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        });
      } else {
        await axios.post("http://localhost:8000/api/courses/", { name, credits }, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        });
      }
      onSuccess();
    } catch (error) {
      console.error("Error saving course:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Nombre del Curso:</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>
      <div>
        <label>Créditos:</label>
        <input
          type="number"
          value={credits}
          onChange={(e) => setCredits(e.target.value)}
          required
        />
      </div>
      <button type="submit">{course.id ? "Actualizar" : "Crear"}</button>
    </form>
  );
};

export default CourseForm;

