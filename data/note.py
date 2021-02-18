from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

from data.db import Base


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    create_date = Column(DateTime)

    def to_dict(self):
        return {'id': self.id, 'content': self.content, 'createDate': self.create_date}
