from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String) //имя пользователя телеграм
    fullname = Column(String) //имя указанное в анкете
    department = Column(String) //отдел
    hobbies = Column(String) //хобби
    expectations = Column(String) //ожидания
