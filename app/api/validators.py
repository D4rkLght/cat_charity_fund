from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charityproject_crud
from app.models import CharityProject, User


async def check_name(
    project_name: str,
    session: AsyncSession,
) -> None:
    project_id = await charityproject_crud.get_chairty_project_id_by_name(project_name, session)
    if project_id is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!',
        )
    if not project_name or len(project_name) > 100:
        raise HTTPException(
            status_code=422,
            detail='Нельзя создавать имя больше 100 символов или не создавать вовсе!',
        )


async def check_charity_project_exists(
    project_id: int,
    session: AsyncSession
) -> CharityProject:
    project = await charityproject_crud.get(project_id, session)
    if project is None:
        raise HTTPException(
            status_code=404,
            detail='Фонд не найден!'
        )
    return project


async def check_investments(
    project_id: int,
    session: AsyncSession
) -> None:
    project = await charityproject_crud.get(project_id, session)
    if project.invested_amount:
        raise HTTPException(
            status_code=422,
            detail=' Нельзя удалить проект, в который уже были инвестированы средства.',
        )


async def check_full_amount(
    project_id: int,
    session: AsyncSession
) -> None:
    project = await charityproject_crud.get(project_id, session)
    if project.full_amount < project.invested_amount:
        raise HTTPException(
            status_code=422,
            detail='Требуемая сумма меньше внесённой.',
        )