"""
This module provides the Article model for the Pyramid Learning Journal project
"""

from sqlalchemy import (
    Column,
    Index,
    Integer,
    UnicodeText,
    DateTime
)

from .meta import Base


class PLJ_Article(Base):
    """
    This is the article model for the pyramid learning journal project.
    It does not require, but should have a title, date_created and body.
    """
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(UnicodeText)
    date_created = Column(DateTime)
    body = Column(UnicodeText)

Index('ljb_index', PLJ_Article.title, unique=True, mysql_length=255)
