from Models.db2 import Base
from sqlalchemy import Column, Integer, DateTime, String
from datetime import datetime

class Orders(Base):

    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, nullable=True)
    name = Column(String(30), nullable=True)
    postal = Column(Integer)
    date = Column(DateTime(), default=datetime.now())
    
    def __init__(self, id_user, name, postal):
        self.id_user = id_user
        self.name = name
        self.postal = postal
        

    

    
