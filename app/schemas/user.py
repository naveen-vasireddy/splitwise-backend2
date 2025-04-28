from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    userId: str
    name: str
    email: EmailStr
    phoneNumber: Optional[str]