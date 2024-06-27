from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .... import models, schemas, crud
from ... import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.UserRoleInDBBase])
def get_user_roles(
        db: Session = Depends(deps.get_db)
) -> list[models.UserRole]:
    """
    Get all user_roles.
    """
    return crud.user_role.get_multi(db)


@router.get("/{id_user_role}", response_model=schemas.UserRoleInDBBase)
def get_user_role(
        db: Session = Depends(deps.get_db),
        *,
        id_user_role: int
) -> models.UserRole:
    """
    Get once user_role.
    """
    user_role = crud.user_role.get(db=db, id=id_user_role)
    if not user_role:
        raise HTTPException(status_code=404, detail="user_role not found")
    return user_role


@router.post("/", response_model=schemas.UserRoleCreate)
def create_user_role(
        *,
        db: Session = Depends(deps.get_db),
        user_role_in: schemas.UserRoleCreate
) -> models.UserRole:
    """
    Create new user_role.
    """
    user_role = crud.user_role.create(db=db, obj_in=user_role_in)
    return user_role


@router.put("/{id_user_role}", response_model=schemas.UserRoleUpdate)
def update_user_role(
        *,
        db: Session = Depends(deps.get_db),
        id_user_role: int,
        user_role_in: schemas.UserRoleUpdate
) -> Any:
    """
    Update an user_role.
    """
    user_role = crud.user_role.get(db=db, id=id_user_role)
    if not user_role:
        raise HTTPException(status_code=404, detail="user_role not found")
    upd_user_role = crud.user_role.update(db=db, db_obj=user_role, obj_in=user_role_in)
    return upd_user_role
