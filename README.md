🎓 School Management Backend API (FastAPI + SQLAlchemy)

This project is a backend API built using FastAPI and SQLAlchemy to manage school data such as students, teachers, and marks.
It includes authentication, role-based access control, and data processing features like percentage calculation and subject-wise toppers.


Features
----------
AUTHENTICATION & AUTHORIZATION

User signup with password hashing and stored in database

Secure login using JWT token

Role-based access (Admin, Teacher, Student)

Protected routes using token verification


USER & ROLE Management 

Create users (default role: student)

Promote user to teacher (admin only)

Role-based access control


STUDENT MANAGMENT

Add students to specific classes

Class-wise data handling (8th, 9th, 10th)

Delete student records


MARKS AND PERFOMANCE

Submit student marks (teacher/admin only)

Fetch student marks

Calculate percentage and grade

Subject-wise top 3 students


TECHNOLOGY

Python,
FastAPI,
SQLAlchemy,
MySQL,
JWT Authentication,

PROJECT STRUCTURE
.
├── main.py              # Entry point

├── routers/             # API routes

├── models/              # Database models

├── dblogic/             # Database operations

├── autho/               # Authentication (JWT)

├── security/            # Password hashing & verification

├── databaseconnect/     # DB connection


👨‍💻 Author

Nigam Gouda
