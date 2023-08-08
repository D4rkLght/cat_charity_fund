from fastapi import APIRouter

from app.api.endpoints import project_router, user_router

main_router = APIRouter()
main_router.include_router(
    project_router, prefix='/charity_project', tags=['Charity project']
)
main_router.include_router(user_router)
