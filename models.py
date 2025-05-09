from sqlalchemy import Column, Integer, String
from router import Base





class User_Master(Base):
    __tablename__ = 'users_master'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class User_Slave(Base):
    __tablename__ = 'users_slave'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)