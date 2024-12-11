import React, { useState, useEffect } from "react";
import axios from "axios";

const CourseLoadForm = () => {
  const [professors, setProfessors] = useState([]);
  const [courses, setCourses] = useState([]);
  const [universities, setUniversities] = useState([]);
  const [careers, setCareers] = useState([]);
  const [professorId, setProfessorId] = useState("");
  const [courseId, setCourseId] = useState("");
  const [universityId, setUniversityId] = useState("");
  const [careerId, setCareerId] = useState("");

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const professorsRes = await axios.get("http://localhost:8000/api/professors/");
    const coursesRes = await axios.get("http://localhost:8000/api/courses/");
    const universitiesRes = await axios.get("http://localhost:8000/api/universities/");
    const careersRes = await axios.get("http://localhost:8000/api/careers/");
    setProfessors(professorsRes.data);
    setCourses(coursesRes.data);
    setUniversities(universitiesRes.data);
    setCareers(careersRes.data);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("http://localhost:8000/api/course_loads/", {
        professor: professorId,
        course: courseId,
        university: universityId,
        career: careerId,
      });
      alert("Carga asignada correctamente");
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <form className="mt-4" onSubmit={handleSubmit}>
      <h2>Asignar Carga Académica</h2>
      <div className="mb-3">
        <label>Profesor:</label>
        <select
          className="form-select"
          value={professorId}
          onChange={(e) => setProfessorId(e.target.value)}
          required
        >
          <option value="">Seleccione un profesor</option>
          {professors.map((professor) => (
            <option key={professor.id} value={professor.id}>
              {professor.name}
            </option>
          ))}
        </select>
      </div>
      <div className="mb-3">
        <label>Curso:</label>
        <select
          className="form-select"
          value={courseId}
          onChange={(e) => setCourseId(e.target.value)}
          required
        >
          <option value="">Seleccione un curso</option>
          {courses.map((course) => (
            <option key={course.id} value={course.id}>
              {course.name}
            </option>
          ))}
        </select>
      </div>
      <div className="mb-3">
        <label>Universidad:</label>
        <select
          className="form-select"
          value={universityId}
          onChange={(e) => setUniversityId(e.target.value)}
          required
        >
          <option value="">Seleccione una universidad</option>
          {universities.map((university) => (
            <option key={university.id} value={university.id}>
              {university.name}
            </option>
          ))}
        </select>
      </div>
      <div className="mb-3">
        <label>Carrera:</label>
        <select
          className="form-select"
          value={careerId}
          onChange={(e) => setCareerId(e.target.value)}
          required
        >
          <option value="">Seleccione una carrera</option>
          {careers.map((career) => (
            <option key={career.id} value={career.id}>
              {career.name}
            </option>
          ))}
        </select>
      </div>
      <button type="submit" className="btn btn-primary">
        Asignar Curso
      </button>
    </form>
  );
};

export default CourseLoadForm;

