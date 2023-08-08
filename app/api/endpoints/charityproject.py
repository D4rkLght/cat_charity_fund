from typing import Dict, List, Set, Tuple
from fastapi import APIRouter, Depends, HTTPException

# Импортируем класс асинхронной сессии для аннотации параметра.

from sqlalchemy.ext.asyncio import AsyncSession

# Импортируем асинхронный генератор сессий.
from app.api.validators import check_name_duplicate, check_charity_project_exists
from app.core.db import get_async_session
from app.crud.charityproject import charityproject_crud
from app.schemas.charityproject import (
    CharityProjectCreate, CharityProjectUpdate, CharityProjectDB
)
from app.core.user import current_superuser

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    # dependencies=[Depends(current_superuser)],
)
async def create_new_charity_project(
    project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    # """Только для суперюзеров."""
    await check_name_duplicate(project.name, session)
    new_project = await charityproject_crud.create(project, session)
    return new_project


@router.get(
    '/',
    response_model=List[CharityProjectDB],
    response_model_exclude_none=True,
)
async def all_charity_projects(
    session: AsyncSession = Depends(get_async_session),
):
    all_projects = await charityproject_crud.get_multi(session)
    return all_projects


@router.delete(
    '/{charity_project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def remove_charity_project(
    charity_project_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    charity_project = await check_charity_project_exists(
        charity_project_id, session
    )
    charity_project = await charityproject_crud.remove(
        charity_project, session
    )
    return charity_project


@router.patch(
    '/{charity_project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
)
async def update_charity_project(
    charity_project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    charity_project = await check_charity_project_exists(
        charity_project_id, session
    )
    if obj_in.name is not None:
        await check_name_duplicate(obj_in.name, session)
    charity_project = await charityproject_crud.update(
        charity_project, obj_in, session
    )
    return charity_project
