from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_charity_project_exists,
                                check_full_amount, check_fully_invested,
                                check_investments, check_project,
                                check_project_name_duplicate)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charityproject_crud
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)
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
    await check_project(project, project.name, session)
    await check_project_name_duplicate(project.name, session)
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
    return await charityproject_crud.get_multi(session)


@router.delete(
    '/{charity_project_id}',
    response_model=CharityProjectDB,
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
    return await charityproject_crud.remove(
        charity_project, session
    )


@router.patch(
    '/{charity_project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def update_charity_project(
    charity_project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    '''Только для суперюзеров.'''
    await check_fully_invested(charity_project_id, session)
    charity_project = await check_charity_project_exists(
        charity_project_id, session
    )
    await check_full_amount(obj_in, charity_project_id, session)
    if obj_in.name is not None:
        await check_project_name_duplicate(obj_in.name, session)
    return await charityproject_crud.update(
        charity_project, obj_in, session
    )
