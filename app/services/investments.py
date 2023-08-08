from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.parent_base import Parent_Base


async def investments(
    model: Parent_Base,
    session: AsyncSession,
):
    model.invested_amount = (model.invested_amount or 0) + model.full_amount
    model.close_date = datetime.now()
    print(model.invested_amount)