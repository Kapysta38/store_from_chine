from ..crud.base import CRUDBase
from ..models import Role
from ..schemas import RoleBase


class CRUDRole(CRUDBase[Role, RoleBase, RoleBase]):
    def __init__(self, model):
        super().__init__(model)


role = CRUDRole(Role)
