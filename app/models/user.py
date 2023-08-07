from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

# Новый импорт.
from sqlalchemy import Column, DateTime, String, Text

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    ...
