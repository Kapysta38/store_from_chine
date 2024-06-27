from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .... import models, schemas, crud
from ... import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.ItemInDBBase])
def get_items(
        db: Session = Depends(deps.get_db)
) -> list[models.Item]:
    """
    Get all items.
    """
    return crud.item.get_multi(db)


@router.get("/{id_item}", response_model=schemas.ItemInDBBase)
def get_item(
        db: Session = Depends(deps.get_db),
        *,
        id_item: int
) -> models.Item:
    """
    Get once item.
    """
    item = crud.item.get(db=db, id=id_item)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=schemas.ItemInDBBase)
def create_item(
        *,
        db: Session = Depends(deps.get_db),
        item_in: schemas.CreateItem
) -> models.Item:
    """
    Create new item.
    """
    item = crud.item.create(db=db, obj_in=item_in)
    return item


@router.put("/{id_item}", response_model=schemas.UpdateItem)
def update_item(
        *,
        db: Session = Depends(deps.get_db),
        id_item: int,
        item_in: schemas.UpdateItem
) -> Any:
    """
    Update an item.
    """
    item = crud.item.get(db=db, id=id_item)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    upd_item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
    return upd_item


@router.delete("/{id_item}", response_model=schemas.ItemInDBBase)
def remove_item(
        *,
        db: Session = Depends(deps.get_db),
        id_item: int,
        item_in: schemas.RemoveItem
) -> models.Item:
    """
    Remove item.
    """
    item = crud.item.get(db=db, id=id_item)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item = crud.item.remove(db=db, id=id_item)
    return item
