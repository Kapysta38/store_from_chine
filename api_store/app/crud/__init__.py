from .crud_item import item
from .crud_user import user
from .crud_order import order
from .crud_role import role
from .crud_user_role import user_role
from .crud_feedback import feedback
# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)