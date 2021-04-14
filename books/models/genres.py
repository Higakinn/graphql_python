from sqlalchemy import Column, Integer, String

from ..database.base import Base


class Genres(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))