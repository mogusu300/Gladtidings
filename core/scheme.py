from pydynatic import Basemodel, EmailStr
from typing import List 

class UserCreateSchema(BaseModel):
  username: str
  email: EmailStr
  password: str
  role: str
