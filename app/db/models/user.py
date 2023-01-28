""" User model """
from sqlalchemy import Column, String, Text, Boolean, Integer
from app.db.base import BasePsql
from app.db.mixins.timestamp_mixin import TimestampMixin

class User(BasePsql, TimestampMixin):
    """ The users table """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=True)
    email = Column(String, nullable=False)
    avatar_url = Column(Text, nullable=False)
    deleted = Column(Boolean, default=False)
