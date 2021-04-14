from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from ..database.base import Base
from ..models.genres import Genres


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    author = Column(String(255))
    genre_id = Column(Integer, ForeignKey('genres.id', ondelete="CASCADE"))
    genre = relationship(
        Genres,
        backref=backref('books', uselist=True, cascade='all,delete-orphan')
    )
     