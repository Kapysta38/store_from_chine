from typing import List, Optional, Type

from sqlalchemy.orm import Session

from ..crud.base import CRUDBase
from ..models import Feedback
from ..schemas import FeedbackCreate, FeedbackUpdate


class CRUDFeedback(CRUDBase[Feedback, FeedbackCreate, FeedbackUpdate]):
    def __init__(self, model):
        super().__init__(model)

    def get_filter(
            self, db: Session,
            *,
            user_id: Optional[int] = None,
    ) -> List[Type[Feedback]]:
        query = db.query(self.model)
        if user_id is not None:
            query = query.filter_by(user_id=user_id)
        return query.all()


feedback = CRUDFeedback(Feedback)
