from sqlalchemy import Column, Integer, DateTime, func, String, ForeignKey
from sqlalchemy.orm import relationship

from ..db.database import Base


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    text = Column(String(255), nullable=False)
    answer = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="feedback")
