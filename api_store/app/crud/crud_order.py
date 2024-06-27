from ..crud.base import CRUDBase
from ..models import Order
from ..schemas import OrderBase


class CRUDOrder(CRUDBase[Order, OrderBase, OrderBase]):
    def __init__(self, model):
        super().__init__(model)


order = CRUDOrder(Order)
