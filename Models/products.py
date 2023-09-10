from Models.db2 import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Products(Base):

    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    id_category = Column(Integer)
    create_at = Column(DateTime(), default=datetime.now())
    update_at = Column(DateTime(), default=datetime.now())

    def __init__(self, name, price, stock, id_category):
        self.name = name
        self.price = price
        self.stock = stock
        self.id_category = id_category
    
   

