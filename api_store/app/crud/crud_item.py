from ..crud.base import CRUDBase
from ..models.item import Item
from ..schemas.item import BaseItem


class CRUDItem(CRUDBase[Item, BaseItem, BaseItem]):
    def __init__(self, model):
        super().__init__(model)


item = CRUDItem(Item)
