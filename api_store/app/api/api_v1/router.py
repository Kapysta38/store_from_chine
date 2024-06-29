from fastapi import APIRouter

from ...api.api_v1.endpoints import item, user, order, user_role, role, feedback

api_router = APIRouter()
api_router.include_router(item.router, prefix='/item', tags=['item'])
api_router.include_router(user.router, prefix='/user', tags=['user'])
api_router.include_router(order.router, prefix='/order', tags=['order'])
api_router.include_router(user_role.router, prefix='/user_role', tags=['user_role'])
api_router.include_router(role.router, prefix='/role', tags=['role'])
api_router.include_router(feedback.router, prefix='/feedback', tags=['feedback'])
