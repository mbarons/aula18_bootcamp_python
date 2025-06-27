from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from db import Base


class Joke(Base):
    __tablename__ = "jokes"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    setup = Column(String)
    punchline = Column(String)
    created_at = Column(DateTime, default=func.now())
