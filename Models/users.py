from Models.db2 import Base
from sqlalchemy import Column, Integer, BigInteger, String, DateTime
from datetime import datetime, date

class Users(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(BigInteger, nullable=False, unique=True)
    date_create = Column(DateTime(), default=date.today())
    date_access = Column(DateTime(), default=datetime.now())
    

    def __init__(self, username, firstname, lastname, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.phone = phone


