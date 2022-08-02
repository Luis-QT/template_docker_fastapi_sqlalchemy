""" User model """
from sqlalchemy import Column, String, Date, Integer, Enum, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import BasePsql
from app.db.mixins.guid_mixin import GuidMixin
from app.db.mixins.timestamp_mixin import TimestampMixin

class User(BasePsql, GuidMixin, TimestampMixin):
    """ The users table """
    __tablename__ = 'users'
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=True)
    email = Column(String, nullable=False)
    status = Column(Integer, default=1)
    avatar_url = Column(Text, nullable=False)
