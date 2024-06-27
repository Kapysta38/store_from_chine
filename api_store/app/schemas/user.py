from typing import Optional, Union
from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    user_id: int
    full_name: Union[str, None]
    address: Union[str, None]
    tg_id: int


class UserCreate(UserBase):
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class UserUpdate(UserBase):
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    tg_id: Optional[int] = None
    address: Union[str, None] = None
    full_name: Union[str, None] = None


class UserInDBBase(UserBase):
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

