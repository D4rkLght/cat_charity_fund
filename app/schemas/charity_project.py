from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt, validator

from app.core.config import MAX_SYMBOLS_NAME, MIN_LENGHT


class CharityProjectCreate(BaseModel):
    name: str = Field(..., max_length=MAX_SYMBOLS_NAME)
    description: Optional[str]
    full_amount: PositiveInt


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=MAX_SYMBOLS_NAME)
    description: Optional[str]
    full_amount: Optional[PositiveInt]

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя проекта не может быть пустым')
        return value

    class Config:
        extra = Extra.forbid
        min_anystr_length = MIN_LENGHT


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
