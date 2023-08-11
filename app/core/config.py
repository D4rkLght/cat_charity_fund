from typing import Optional

from pydantic import BaseSettings, EmailStr

MAX_SYMBOLS_NAME = 100
MAX_TIME_OF_ACTION_JWT = 3600
MIN_LENGHT = 1
NO_INVESTED = 0


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
