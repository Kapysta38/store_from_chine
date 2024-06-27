from ..crud.base import CRUDBase
from ..models import UserRole
from ..schemas import UserRoleBase


class CRUDUserRole(CRUDBase[UserRole, UserRoleBase, UserRoleBase]):
    def __init__(self, model):
        super().__init__(model)


user_role = CRUDUserRole(UserRole)
