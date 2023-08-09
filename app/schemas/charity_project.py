from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt, Extra, validator


class CharityProjectBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str]
    full_amount: PositiveInt


class CharityProjectCreate(CharityProjectBase):
    ...


class CharityProjectUpdate(CharityProjectBase):
    name: Optional[str] = Field(None, max_length=100)

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя проекта не может быть пустым')
        return value


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
