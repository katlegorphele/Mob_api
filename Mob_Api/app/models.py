from sqlalchemy import Column, Integer, String
from .database import Base

class Mob_Agent(Base):
    __tablename__ = 'mob_agents'
    id = Column(Integer, primary_key=True, index=True)
    name_sur = Column(String)
    email = Column(String)
    password = Column(String)

class Mob_Spectator(Base):
    __tablename__ = 'mob_spectators'
    id = Column(Integer, primary_key=True, index=True)
    name_sur = Column(String)
    email = Column(String)
    password = Column(String)
