from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Благотворительная поддержка'
    database_url: str
    db_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    path: str
    description: str = 'Описание'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
