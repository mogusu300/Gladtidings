from pydantic import BaseModel
from typing import List, Optional

class UserCreateSchema(BaseModel):
    username: str
    email: str
    password: str
    role: str

    class Config:
        from_attributes = True

class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True

class LoginSchema(BaseModel):
    username: str
    password: str

class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str

class CourseSchema(BaseModel):
    id: int
    title: str
    description: str
    public: bool

    class Config:
        from_attributes = True

class TopicSchema(BaseModel):
    id: int
    title: str
    content: str
    course_id: int

    class Config:
        from_attributes = True

class EnrollmentSchema(BaseModel):
    user_id: int
    course_id: int

    class Config:
        from_attributes = True

class CertificateSchema(BaseModel):
    id: int
    user_id: int
    course_id: int
    issued_at: str

    class Config:
        from_attributes = True






