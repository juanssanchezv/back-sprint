from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db_connection import Base, engine


class UserInDB(Base):
    __tablename__ = "users"

    username    = Column(String, primary_key=True, unique=True)
    password    = Column(String)


Base.metadata.create_all(bind=engine)
