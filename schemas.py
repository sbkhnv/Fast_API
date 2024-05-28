from pydantic import BaseModel
from typing import Optional

class RegisterModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]


    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "first_name": "John",
                "last_name": "Doe",
                "username": "johndoe",
                "paasword": "password",
                "emai": "envkt@example.com",
                "is_staff": True,
                "is_active": True
            }
        }



class LoginModel(BaseModel):
    username: str
    password: str


