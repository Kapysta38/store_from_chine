from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from ..db.database import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=True)
    address = Column(String(255), nullable=True)
    tg_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())

    orders = relationship("Order", back_populates="user")
    user_roles = relationship("UserRole", back_populates="user")