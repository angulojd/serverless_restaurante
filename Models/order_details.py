from Models.db2 import Base
from sqlalchemy import Column, Integer

class Details(Base):
    __tablename__ = 'order_detail'
    id = Column(Integer, primary_key=True)
    id_orden = Column(Integer, nullable=False)
    id_product = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)


    def __init__(self, id_orden, id_product, quantity, price):
        self.id_orden = id_orden
        self.id_product = id_product
        self.quantity = quantity
        self.price = price

    
