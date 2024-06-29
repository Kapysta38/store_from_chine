from typing import List, Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .... import models, schemas, crud
from ... import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.FeedbackInDBBase])
def get_feedbacks(
        db: Session = Depends(deps.get_db),
        user_id: Optional[int] = None,
) -> list[models.Feedback]:
    """
    Get all feedbacks.
    """
    return crud.feedback.get_filter(db, user_id=user_id)


@router.get("/{id_feedback}", response_model=schemas.FeedbackInDBBase)
def get_feedback(
        db: Session = Depends(deps.get_db),
        *,
        id_feedback: int
) -> models.Feedback:
    """
    Get once feedback.
    """
    feedback = crud.feedback.get(db=db, id=id_feedback)
    if not feedback:
        raise HTTPException(status_code=404, detail="feedback not found")
    return feedback


@router.post("/", response_model=schemas.FeedbackCreate)
def create_feedback(
        *,
        db: Session = Depends(deps.get_db),
        feedback_in: schemas.FeedbackCreate
) -> models.Feedback:
    """
    Create new feedback.
    """
    feedback = crud.feedback.create(db=db, obj_in=feedback_in)
    return feedback


@router.put("/{id_feedback}", response_model=schemas.FeedbackUpdate)
def update_feedback(
        *,
        db: Session = Depends(deps.get_db),
        id_feedback: int,
        feedback_in: schemas.FeedbackUpdate
) -> Any:
    """
    Update an feedback.
    """
    feedback = crud.feedback.get(db=db, id=id_feedback)
    if not feedback:
        raise HTTPException(status_code=404, detail="feedback not found")
    upd_feedback = crud.feedback.update(db=db, db_obj=feedback, obj_in=feedback_in)
    return upd_feedback
