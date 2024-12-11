# PROYECTO-FINAL-IWEB
# Gestión Académica

## Descripción
Este proyecto es una aplicación web para gestionar la carga académica de universidades. Permite:
- **Listar Profesores** con opciones para agregar, editar y eliminar.
- **Listar Cursos** con opciones para crear, editar y eliminar.
- **Asignar Carga Académica** a profesores en cursos específicos, considerando universidad y carrera.

La aplicación se desarrolla con un **backend** en Django (usando Django REST Framework) y un **frontend** en React. El diseño utiliza Bootstrap para lograr una interfaz intuitiva y atractiva.

---

## Instalación

### Backend
1. Clona el repositorio:
   # ```bash
   git clone <URL-del-repositorio>
   cd backend

### Crea un entorno virtual e instálalo

python -m venv venv
source venv/bin/activate # o venv\Scripts\activate en Windows
pip install -r requirements.txt

### Configurar la base de datos:
Usuario: iweb
Contraseña: sjbdls
Base de datos: sisacad

### Realiza las migraciones y ejecuta el servidor:
python manage.py migrate
python manage.py runserver

### Captura 1
![Captura de Pantalla 1](./Captura%20de%20pantalla%202024-12-11%20145854.png)


## INTERFAZ

### Instalar las dependencias:

npm install

### Ejecuta el servidor de desarrollo

npm start

# Imagenes
### Captura 2
![Captura de Pantalla 2](./Captura%20de%20pantalla%202024-12-11%20145908.png)

# Estructura del Proyecto

 project/
├── backend/
│   ├── manage.py
│   ├── api/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   └── urls.py
│   └── settings.py
├── frontend/
│   ├── public/
│   │   └── images/
│   │       └── academic_management.jpg
│   ├── src/
│   │   ├── components/
│   │   │   ├── ProfessorList.js
│   │   │   ├── CourseList.js
│   │   │   └── CourseLoadForm.js
│   │   └── App.js
├── README.md
└── requirements.txt


# TECNOLOGIAS USADAS

Backend : Django, marco de trabajo Django REST
Interfaz : React, Bootstrap
Base de datos : MySQL (phpMyAdmin)

# AUTOR
Proyecto desarrollado por Esthephany Chqoeuhuanca Layme 🎓



# PROYECTO-FINAL-IWEB



