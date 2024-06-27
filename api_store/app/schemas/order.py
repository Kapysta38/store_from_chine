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
    order_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class OrderUpdate(OrderBase):
    user_id: Optional[int] = None
    product_url: Optional[str] = None
    order_id: Optional[int] = None
    order_status: StatusOrder = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class OrderInDBBase(OrderBase):
    order_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
