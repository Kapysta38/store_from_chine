from typing import Optional, Union
from datetime import datetime

from pydantic import BaseModel


class FeedbackBase(BaseModel):
    id: int
    user_id: int
    text: str
    answer: Union[str, None]


class FeedbackCreate(FeedbackBase):
    id: int = None
    answer: Union[str, None] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class FeedbackUpdate(FeedbackBase):
    id: int = None
    text: str = None
    answer: Union[str, None] = None
    user_id: int = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class FeedbackInDBBase(FeedbackBase):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
