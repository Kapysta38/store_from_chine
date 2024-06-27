from typing import List, Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .... import models, schemas, crud
from ... import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.OrderInDBBase])
def get_orders(
        db: Session = Depends(deps.get_db),
        user_id: Optional[int] = None,
        product_url: Optional[str] = None,
        order_status: Optional[str] = None,
        today: bool = False,
) -> list[models.Order]:
    """
    Get all orders.
    """
    return crud.order.get_filter(db, user_id=user_id, product_url=product_url, order_status=order_status,
                                 today=today)


@router.get("/{id_order}", response_model=schemas.OrderInDBBase)
def get_order(
        db: Session = Depends(deps.get_db),
        *,
        id_order: int
) -> models.Order:
    """
    Get once order.
    """
    order = crud.order.get(db=db, id=id_order)
    if not order:
        raise HTTPException(status_code=404, detail="order not found")
    return order


@router.post("/", response_model=schemas.OrderCreate)
def create_order(
        *,
        db: Session = Depends(deps.get_db),
        order_in: schemas.OrderCreate
) -> models.Order:
    """
    Create new order.
    """
    order = crud.order.create(db=db, obj_in=order_in)
    return order


@router.put("/{id_order}", response_model=schemas.OrderUpdate)
def update_order(
        *,
        db: Session = Depends(deps.get_db),
        id_order: int,
        order_in: schemas.OrderUpdate
) -> Any:
    """
    Update an order.
    """
    order = crud.order.get(db=db, id=id_order)
    if not order:
        raise HTTPException(status_code=404, detail="order not found")
    upd_order = crud.order.update(db=db, db_obj=order, obj_in=order_in)
    return upd_order
