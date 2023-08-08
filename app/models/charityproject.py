from sqlalchemy import Column, String, Text

from .parent_base import Parent_Base


class CharityProject(Parent_Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
