from typing import Dict, List, Set, Tuple
from fastapi import APIRouter, Depends, HTTPException

# Импортируем класс асинхронной сессии для аннотации параметра.

from sqlalchemy.ext.asyncio import AsyncSession

# Импортируем асинхронный генератор сессий.
from app.api.validators import check_project, check_charity_project_exists
from app.core.db import get_async_session
from app.crud.donation import donation_crud
from app.schemas.donation import (
    DonationCreate, DonationShortDB, DonationDB
)
from app.core.user import current_superuser, current_user
from app.models import User
from app.services.investments import investments

router = APIRouter()


@router.post(
    '/',
    response_model=DonationShortDB,
    response_model_exclude_none=True,
)
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    new_donation = await donation_crud.create(donation, session, user)
    session.add_all(await investments(new_donation, session))
    await session.commit()
    await session.refresh(new_donation)
    return new_donation


@router.get(
    '/',
    response_model=List[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    '''Только для суперюзеров.'''
    all_donations = await donation_crud.get_multi(session)
    return all_donations


@router.get(
    '/my/',
    response_model=List[DonationShortDB],
    response_model_exclude_none=True,
)
async def get_my_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    my_donations = await donation_crud.get_multi_my(session=session, user=user)
    return my_donations