from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt, Extra, validator


class CharityProjectCreate(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str]
    full_amount: PositiveInt


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str]
    full_amount: Optional[PositiveInt]

    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Имя проекта не может быть пустым')
        return value

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1

class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
