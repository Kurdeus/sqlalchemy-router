from sqlalchemy import Column, Integer, String
from router import MasterBase, SlaveBase





class User_Master(MasterBase):
    __tablename__ = 'users_master'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class User_Slave(SlaveBase):
    __tablename__ = 'users_slave'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)