from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charityproject import charityproject_crud
from app.models import CharityProject, User


async def check_name_duplicate(
    room_name: str,
    session: AsyncSession,
) -> None:
    room_id = await charityproject_crud.get_chairty_project_id_by_name(room_name, session)
    if room_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Благотворительный проект с таким именем уже существует!',
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
