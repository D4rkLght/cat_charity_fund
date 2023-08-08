from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.models.donation import Donation


class CRUDDonation(CRUDBase):
   ...


donation_crud = CRUDDonation(Donation)
