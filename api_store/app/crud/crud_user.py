from ..crud.base import CRUDBase
from ..models import User
from ..schemas import UserBase


class CRUDUser(CRUDBase[User, UserBase, UserBase]):
    def __init__(self, model):
        super().__init__(model)


user = CRUDUser(User)
