from typing import Optional

from pydantic import BaseModel

from ..shared.types import Rating


class BaseItem(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    rating: Rating


class ItemInDBBase(BaseItem):
    id: Optional[int] = None

    class Config:
        from_attributes = True


class CreateItem(BaseItem):
    pass


class UpdateItem(BaseItem):
    pass


class RemoveItem(BaseItem):
    pass
