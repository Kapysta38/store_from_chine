from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from ..shared.types import StatusOrder


class OrderBase(BaseModel):
    order_id: int
    user_id: int
    product_url: str
    order_status: StatusOrder = StatusOrder.created


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass


class OrderInDBBase(OrderBase):
    order_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
