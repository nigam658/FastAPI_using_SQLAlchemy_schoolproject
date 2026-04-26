from sqlalchemy.orm import Session
from fastapi import HTTPException
import SQLTable
from sqlalchemy.exc import IntegrityError
from model import student_mark


# signup user 
def signup_user(db:Session, name:str, pwd : str, role : str):
    try:
        new_user = SQLTable.check_student(username = name, password = pwd, role = role)

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="username already exists")
    
#access user for cheking user exist or not from user_pass table
def access_user(db: Session, username : str):

    user = db.query(SQLTable.check_student).filter(SQLTable.check_student.username == username).first()
    return user


# store teacher details
def create_teacher(db: Session, name: str):
    name = name.strip()

    user = db.query(SQLTable.check_student).filter(SQLTable.check_student.username == name).first()

    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    if user.role == "teacher":
        raise HTTPException(status_code=400, detail="already a teacher")

    user.role = "teacher"

    db.commit()
    db.refresh(user)

    return user



# insert student details with class_wise
def add_student (db:Session, classs : str, name:str):
    if classs == "class_8th":
        username = SQLTable.class8th(student_name = name)
    elif classs == "class_9th":
        username = SQLTable.class9th(student_name = name)
    elif classs == "class_10th":
        username = SQLTable.class10th(student_name = name)

    db.add(username)
    db.commit()
    db.refresh(username)
    
    return username

# submit student mark
def add_student_mark(db:Session,rollno : int, classs:str, data : student_mark):
    def get_class_table(classs: str):
        if classs == "class_8th":
            return SQLTable.class8th
        elif classs == "class_9th":
            return SQLTable.class9th
        elif classs == "class_10th":
            return SQLTable.class10th
        else:
            return None
    
    Table = get_class_table(classs)

    if not Table :
        raise HTTPException(status_code=404, detail="class not found!")
    
    student = db.query(Table).filter(Table.student_rollno == rollno).first()

    if not student :
        raise HTTPException(status_code=404, detail="student not found")
    
    for key, value in data.dict().items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    return student


def collect_student_mark (db:Session,classs:str,rollno:int):
    def get_class_table(classs: str):
        if classs == "class_8th":
            return SQLTable.class8th
        elif classs == "class_9th":
            return SQLTable.class9th
        elif classs == "class_10th":
            return SQLTable.class10th
        else:
            return None
    
    Table = get_class_table(classs)

    student_details = db.query(Table.student_name,
    Table.Physics,
    Table.Chemistry,
    Table.Math,
    Table.English,
    Table.Biology,
    Table.IT).filter(Table.student_rollno == rollno).first()

    if not student_details :
        raise HTTPException(status_code=404,details = "student not found")
    
    return student_details

#collect top 3 studnet a specific class
def collect_top3(db:Session,classs:str, subject:str):
    def get_class_table(classs: str):
        if classs == "class_8th":
            return SQLTable.class8th
        elif classs == "class_9th":
            return SQLTable.class9th
        elif classs == "class_10th":
            return SQLTable.class10th
        else:
            return None
    
    Table = get_class_table(classs)
    if not Table:
        raise HTTPException(404, "class not found")

    column = getattr(Table, subject)

    top3 = db.query(Table).order_by(column.desc()).limit(3).all()

    return top3

# delete specific user 
def delete_users(db:Session, classs : str, rollno : int):
    def get_class_table(classs: str):
        if classs == "class_8th":
            return SQLTable.class8th
        elif classs == "class_9th":
            return SQLTable.class9th
        elif classs == "class_10th":
            return SQLTable.class10th
        else:
            return None
    
    Table = get_class_table(classs)

    student = db.query(Table).filter(Table.student_rollno == rollno).first()

    if not student :
        raise HTTPException(status_code=404, detail = "user not found!")
    

    db.delete(student)
    db.commit()

    return {"message": "student deleted successfully"}
