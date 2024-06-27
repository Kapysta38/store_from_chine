from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from ..shared.types import Roles


class RoleBase(BaseModel):
    role_id: int
    role_name: Roles


class RoleCreate(RoleBase):
    pass


class RoleUpdate(RoleBase):
    pass


class RoleInDBBase(RoleBase):
    role_id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
