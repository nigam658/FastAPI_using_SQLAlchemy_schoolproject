from sqlalchemy import String, Integer, Column,Numeric
from databaseconnect import base

class Teacher (base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    teachername = Column(String(50))
    subject =Column(String(50))

class check_student(base):
    __tablename__ = "user_pass"

    id = Column(Integer,primary_key=True, index=True, autoincrement=True)
    username = Column(String(50),unique=True)
    password = Column(String(500))
    role = Column(String(50))

#class 8th table
class class8th(base):
    __tablename__ = "class_8th"

    id = Column(Integer,primary_key=True,autoincrement=True)
    student_name = Column(String(50))
    student_rollno = Column(Integer, unique=True)
    Physics = Column(Numeric (5, 2))
    Chemistry = Column(Numeric(5, 2))
    Math = Column(Numeric (5, 2))
    English = Column(Numeric (5, 2))
    Biology = Column(Numeric (5, 2))
    IT = Column(Numeric (5, 2))

#class 9th table
class class9th(base):
    __tablename__ = "class_9th"

    id = Column(Integer,primary_key=True,autoincrement=True)
    student_name = Column(String(50))
    student_rollno = Column(Integer, unique=True)
    Physics = Column(Numeric (5, 2))
    Chemistry = Column(Numeric(5, 2))
    Math = Column(Numeric (5, 2))
    English = Column(Numeric (5, 2))
    Biology = Column(Numeric (5, 2))
    IT = Column(Numeric (5, 2))

#class 10th table 
class class10th(base):
    __tablename__ = "class_10th"

    id = Column(Integer,primary_key=True,autoincrement=True)
    student_name = Column(String(50))
    student_rollno = Column(Integer, unique=True)
    Physics = Column(Numeric (5, 2))
    Chemistry = Column(Numeric(5, 2))
    Math = Column(Numeric (5, 2))
    English = Column(Numeric (5, 2))
    Biology = Column(Numeric (5, 2))
    IT = Column(Numeric (5, 2))