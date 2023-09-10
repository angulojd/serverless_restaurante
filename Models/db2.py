from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database\database.s3db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()