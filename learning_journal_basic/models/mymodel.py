from sqlalchemy import (
    Column,
    Index,
    Integer,
    UnicodeText,
    DateTime
)

from .meta import Base


class PLJ_Article(Base):
    import pdb; pdb.set_trace
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(UnicodeText)
    date_created = Column(DateTime)
    body = Column(UnicodeText)

Index('ljb_index', PLJ_Article.title, unique=True, mysql_length=255)
