from sqlalchemy import Column, Integer, Enum, DateTime, func, Text, ForeignKey
from sqlalchemy.orm import relationship

from ..db.database import Base
from ..shared.types import StatusOrder


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    product_url = Column(Text, nullable=False)
    # order_status: 0 - заказ создан, 1 - заказ подтвержден, 2 - невозможно заказать
    order_status = Column(Enum(StatusOrder), default=StatusOrder.created)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="orders")
