from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Event(Base):
    __tablename__ = "event"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("telegram_user.id"), unique=True) //кому дарят
    santa_id = Column(Integer, ForeignKey("telegram_user.id"), unique=True) //кто дарит
