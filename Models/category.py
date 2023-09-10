from Models.db2 import Base
from sqlalchemy import Column, Integer, String

class Categories(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(50))

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    
