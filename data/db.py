from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from utils.load_config import load_config

Base = declarative_base()


engine = create_engine(load_config()['database'], echo=True)
Session = sessionmaker(bind=engine)
