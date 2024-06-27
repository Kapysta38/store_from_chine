from sqlalchemy import Column, Integer, String, Float, Enum

from ..db.database import Base
from ..shared.types import Rating


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    tax = Column(Float, nullable=True)
    rating = Column(Enum(Rating), nullable=False)
