from sqlalchemy import Column, Text, ForeignKey, Integer

from .parent_base import Parent_Base


class Donation(Parent_Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
