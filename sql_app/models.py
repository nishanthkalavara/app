from sqlalchemy import Column, Integer, String
from .database import Base


class User(Base):
    __tablename__ = "memes"

    id = Column(Integer, primary_key=True, index=True)
    name= Column(String)
    url = Column(String)
    caption = Column(String)
    

