from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from ..shared.types import Roles


class RoleBase(BaseModel):
    role_id: int
    role_name: Roles


class RoleCreate(RoleBase):
    role_id: Optional[int] = None


class RoleUpdate(RoleBase):
    role_name: Roles = None
    role_id: Optional[int] = None


class RoleInDBBase(RoleBase):
    role_id: Optional[int] = None

    class Config:
        from_attributes = True
