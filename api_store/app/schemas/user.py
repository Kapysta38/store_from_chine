from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    user_id: int
    full_name: str
    address: str
    tg_id: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True

