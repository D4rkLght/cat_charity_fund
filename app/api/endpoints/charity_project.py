from typing import Dict, List, Set, Tuple
from fastapi import APIRouter, Depends, HTTPException

# Импортируем класс асинхронной сессии для аннотации параметра.

from sqlalchemy.ext.asyncio import AsyncSession

# Импортируем асинхронный генератор сессий.
from app.api.validators import check_name, check_charity_project_exists, check_investments, check_full_amount
from app.core.db import get_async_session
from app.crud.charity_project import charityproject_crud
from app.schemas.charity_project import (
    CharityProjectCreate, CharityProjectUpdate, CharityProjectDB
)
from app.core.user import current_superuser
from app.services.investments import investments

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_new_charity_project(
    project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
):
    '''Только для суперюзеров.'''
    await check_name(project.name, session)
    new_project = await charityproject_crud.create(project, session)
    session.add_all(await investments(new_project, session))
    await session.commit()
    await session.refresh(new_project)
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
    dependencies=[Depends(current_superuser)],
)
async def remove_charity_project(
    charity_project_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    '''Только для суперюзеров.'''
    charity_project = await check_charity_project_exists(
        charity_project_id, session
    )
    await check_investments(charity_project_id, session)
    charity_project = await charityproject_crud.remove(
        charity_project, session
    )
    return charity_project


@router.patch(
    '/{charity_project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
    charity_project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    '''Только для суперюзеров.'''
    charity_project = await check_charity_project_exists(
        charity_project_id, session
    )
    await check_full_amount(charity_project_id, session)
    if obj_in.name is not None:
        await check_name(obj_in.name, session)
    charity_project = await charityproject_crud.update(
        charity_project, obj_in, session
    )
    return charity_project
