from fastapi import APIRouter, HTTPException, Depends,status
from databaseconnect import get_db
from model import Student, student_mark,responsepercentage,SignupreqModel,SignupResponse, LoginreqModel, LoginResponse, promotTeacherReqModel,promotTeacherRespModel,markUpdateResponseModel,CreateTeacherReq,CreateTeacherRes
from logic import calculate_percentage, calculate_grade, my_classes
from autho import create_access_token, get_current_user
from security import hash_password, verify_password
import mysql.connector
import dblogic
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/signup", response_model = SignupResponse)
def signup(signup : SignupreqModel, db: Session = Depends(get_db)):

    role = "student"   # giving to all role as student so bydefult everyone see only only data as a student 
    hassed_pass = hash_password(signup.password)   # convert pain password to hasses password

    user = dblogic.access_user(db,signup.username)
    if user :
        raise HTTPException(status_code=400, detail="username already exist")  # first check if user exist block code , error handeling
        
    newuser = dblogic.signup_user(db,signup.username, hassed_pass,role) 
    
    return {"message" : "signup done ",
            "username" : newuser.username}

#login
@router.post("/login", response_model= LoginResponse)
def login (data : LoginreqModel, db: Session = Depends(get_db)):
 
    db_user = dblogic.access_user(db, data.username)
    
    if not db_user or not verify_password(data.password, db_user.password):
        raise HTTPException(status_code=40, detail="invalid credentials")
    
    role = db_user.role

    token = create_access_token({"sub":data.username, "role" : role}) 

    return {
        "access_token" : token,
        "token_type" : "bearer",
        "role" : role
    }
        
    
@router.post ("/Teachercreate", response_model=CreateTeacherRes)
def Teachercreate(data:CreateTeacherReq, db : Session = Depends(get_db), user : Session = Depends(get_current_user)):

    if user["role"] != "admin" :
        raise HTTPException(status_code=403,detail="you cannot delete data")

    try:
        teacher = dblogic.create_teacher(db, data.teachername)

        return {
            "teachername" : teacher.username
        }
    
    except Exception as e:
        raise e
    
    except Exception as e:
        print("ERROR:", e)  
        raise HTTPException(status_code=500, detail=str(e))   


# joining student 
@router.post("/join/{Classs}",)  
def joining(student:Student, Classs : str, db : Session = Depends(get_db), user : Session = Depends(get_current_user) ):
    
    my_class = my_classes()   # for prevent error,no one can write anything , importe logic file
    
    if Classs not in my_class or user["role"] != "admin" :
        raise HTTPException(status_code=400, detail="invalid credentials")  # use status code to define which type of error
    

    try:
        result = dblogic.add_student(db,Classs,student.name)
        if result:
            return {
                "message" : "student added successfully",
                "data" : result
                }
    
    except :
        return {}

    
        

# store marks
@router.put("/{rollno}/{classs}",response_model=markUpdateResponseModel)
def mark_submit (rollno:int ,classs:str, Students_mark : student_mark,db:Session = Depends(get_db), user : dict = Depends(get_current_user)): # assign student_subject
    
    my_class = my_classes() # for prevent error,no one can write anything , importe logic file

    if classs not in my_class:
        return {"message":"class is not found!"}
    
    if user["role"] not in  ["admin","teacher"] :   #check who is user 
        raise HTTPException(status_code=403, detail="you cannot submit marks") 
    
    try:
        submiting_mark = dblogic.add_student_mark(db, rollno, classs, Students_mark)

        return {"message" : "mark submited"}
    
    except HTTPException as e:
        raise e  

    except:
        raise HTTPException(status_code=500, detail="something went wrong")
     

#return percentage  
@router.get ("/percentage/{classs}/{rollno}", response_model = responsepercentage)
def precentage(classs:str, rollno:int, db:Session=Depends(get_db)):

    my_class = my_classes()  # for prevent error,no one can write anything , importe logic file

    if classs not in my_class:
        raise HTTPException(status_code=404, detail="class not found!")


    student_details = dblogic.collect_student_mark(db,classs,rollno)  # collect student mark

    if not student_details :
        raise HTTPException(status_code=404, detail="user not found!")

    username = student_details[0]
    marks = [float(m) for m in student_details[1:] if m is not None]
    if not marks:
        raise HTTPException(status_code=400, detail="mark not avilable")
    percentage = round(calculate_percentage(marks),2)
    grade = calculate_grade(percentage)
    
    return{
        "username" : username,
        "percentage":percentage,
        "grade":grade
            
        }

# student topper as per subject 
@router.get("/subjecttopper/{classs}/{subject}")
def sub_toper(classs:str, subject : str,db:Session=Depends(get_db)):
    
    my_class = my_classes()
    if classs not in my_class:
        return {"massage" : "class is not found!"}

    try:

        top_3 = dblogic.collect_top3(db, classs, subject)

        # convert to JSON (IMPORTANT)
        result = []
        for student in top_3:
            result.append({
                "name": student.student_name,
                "rollno": student.student_rollno,
                "marks": getattr(student, subject)
            })

        return {"data": result}   
    
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))
    

@router.delete("/{classes}/{rollno}")
def del_user_id (classes : str, rollno : int, user : dict = Depends(get_current_user), db: Session=Depends(get_db) ):

    my_class = my_classes()  # for prevent error,no one can write anything , importe logic file

    if classes not in my_class:
        return {"massage" : "class is not found!"}
    
    if user["role"] != "admin" :
        raise HTTPException(status_code=403,detail="you cannot delete data")
    
    try:
        delete_user = dblogic.delete_users(db,classes,rollno)
        return delete_user
    
    except HTTPException as e:
        raise e
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

        


    
    

    



    

   
