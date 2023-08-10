from datetime import datetime
from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charityproject_crud
from app.crud.donation import donation_crud
from app.models.donation import Donation
from app.models.parent_base import Parent_Base


def update(
    model: Parent_Base,
    amount: int
) -> None:
    model.invested_amount = (model.invested_amount or 0) + amount
    if model.full_amount == model.invested_amount:
        model.close_date = datetime.now()
        model.fully_invested = True


async def investments(
    model: Parent_Base,
    session: AsyncSession,
) -> List[Optional[Parent_Base]]:
    update_object = []
    crud = [donation_crud, charityproject_crud][isinstance(model, Donation)]
    for objects in await crud.get_objects(session):
        amount = min(
            objects.full_amount - (objects.invested_amount or 0),
            model.full_amount - (model.invested_amount or 0)
        )
        update(model, amount)
        update(objects, amount)
        update_object.append(objects)
    return update_object
