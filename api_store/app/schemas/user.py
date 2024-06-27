from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    user_id: int
    full_name: str
    address: str
    tg_id: int


class UserCreate(UserBase):
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    full_name: str = None
    address: str = None


class UserUpdate(UserBase):
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    tg_id: Optional[int] = None
    address: Optional[str] = None
    full_name: Optional[str] = None


class UserInDBBase(UserBase):
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True

