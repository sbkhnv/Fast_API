from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

ENGINE = create_engine('postgresql://postgres:7777@localhost/fast_01', echo=True)

Base = declarative_base()
session = sessionmaker()



