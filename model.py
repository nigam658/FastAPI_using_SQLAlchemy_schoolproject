from pydantic import BaseModel, Field


#join student pydantic model
class Student (BaseModel):
    name: str
    

    class Config :
        extra = "forbid"

class StudentJoinResponseModel (BaseModel):
    message:str
    data : Student

    class Config :
        extra = "forbid"

class student_mark (BaseModel):
    Physics : float = Field(ge=0, le=100)
    Chemistry : float = Field(ge=0, le=100)
    Math : float = Field(ge=0, le=100)
    English : float = Field(ge=0, le=100)
    Biology : float = Field(ge=0, le=100)
    IT : float = Field(ge=0, le=100)

    class Config :
        extra = "forbid"

class responsepercentage (BaseModel):
    username : str
    percentage : float
    grade : str

    class Config :
        extra = "forbid"


#signup pydantic model 
class SignupreqModel(BaseModel):
    username : str = Field(..., min_length=3 )
    password : str = Field(..., min_length=6,pattern="^[a-zA-Z0-9@._-]+$")

    class Config :
        extra = "forbid"

class SignupResponse(BaseModel):
    message : str
    username : str

    class Config :
        extra = "forbid"


#login pydantic model
class LoginreqModel (BaseModel):
    username : str = Field(..., min_length=3)
    password : str = Field(..., min_length=6)

    class Config :
        extra = "forbid"

class LoginResponse (BaseModel):
    access_token : str
    token_type : str
    role : str

    class Config :
        extra = "forbid"

# create teacher pydantic model
class promotTeacherReqModel (BaseModel):
    teacher_name : str = Field(..., min_length=5)

    class Config :
        extra = "forbid"

class promotTeacherRespModel (BaseModel):
    message : str 
    username : str 

    class Config :
        extra = "forbid"


class markUpdateResponseModel(BaseModel):
    message : str

    class Config :
        extra = "forbid"

#create teacherlist
class CreateTeacherReq (BaseModel):
    teachername : str = Field(min_length=5)
    

class CreateTeacherRes (BaseModel):
    teachername : str
    

    class Config:
        extra = "forbid" 
