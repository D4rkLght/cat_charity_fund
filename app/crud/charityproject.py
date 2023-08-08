from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.charityproject import CharityProject
from app.schemas.charityproject import CharityProjectCreate, CharityProjectUpdate


class CRUDCharityProject(CRUDBase[
    CharityProject,
    CharityProjectCreate,
    CharityProjectUpdate
]):
    async def get_chairty_project_id_by_name(
        self,
        room_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        db_room_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == room_name
            )
        )
        db_room_id = db_room_id.scalars().first()
        return db_room_id


charityproject_crud = CRUDCharityProject(CharityProject)
