from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

# User Create Schema
class UserCreateSchema(BaseModel):
    username: str = Field(..., description="The user's username")
    email: EmailStr = Field(..., description="The user's email address")
    password: str = Field(..., description="The user's password")
    role: str = Field(..., description="The user's role")

# User Schema
class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str

    class Config:
        orm_mode = True

# Login Schema
class LoginSchema(BaseModel):
    username: str
    password: str

# Change Password Schema
class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str

# Course Schema
class CourseSchema(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    public: bool
    creator_id: int

    class Config:
        orm_mode = True

# Topic Schema
class TopicSchema(BaseModel):
    id: Optional[int] = None
    course_id: int
    title: str
    content: str

    class Config:
        orm_mode = True

# Enrollment Schema
class EnrollmentSchema(BaseModel):
    id: Optional[int] = None
    user_id: int
    course_id: int

    class Config:
        orm_mode = True

# Certificate Schema
class CertificateSchema(BaseModel):
    id: Optional[int] = None
    user_id: int
    course_id: int
    issue_date: str

    class Config:
        orm_mode = True





