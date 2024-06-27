from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class UserRoleBase(BaseModel):
    user_id: int
    role_id: int


class UserRoleCreate(UserRoleBase):
    pass


class UserRoleUpdate(UserRoleBase):
    pass


class UserRoleInDBBase(UserRoleBase):
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
