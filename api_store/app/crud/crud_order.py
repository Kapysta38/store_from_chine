from typing import Any, List, Optional, Type
import datetime

from sqlalchemy.orm import Session

from ..crud.base import CRUDBase
from ..models import Order
from ..schemas import OrderCreate, OrderUpdate


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):
    def __init__(self, model):
        super().__init__(model)

    def get(self, db: Session, id: Any):
        return db.query(self.model).filter(self.model.order_id == id).first()

    def get_filter(
            self, db: Session,
            *,
            user_id: Optional[int] = None,
            product_url: Optional[str] = None,
            order_status: Optional[str] = None,
            today: bool = False
    ) -> List[Type[Order]]:
        query = db.query(self.model)
        if user_id is not None:
            query = query.filter_by(user_id=user_id)
        if product_url is not None:
            query = query.filter_by(product_url=product_url)
        if order_status is not None:
            query = query.filter_by(order_status=order_status)
        if today:
            now = datetime.datetime.now().date()
            query = query.filter(self.model.created_at.between(
                datetime.datetime.strptime(f"{now} 00:00", "%Y-%m-%d %H:%M"),
                datetime.datetime.strptime(f"{now} 23:59", "%Y-%m-%d %H:%M")
            ))
        return query.all()


order = CRUDOrder(Order)
