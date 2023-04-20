from sqlalchemy import create_engine

engine = create_engine('sqlite:///mydb.sqlite', echo=True)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()

class Resource(Base):
    __tablename__ = "resource"  # DB tabelnaam

    id = Column(Integer, primary_key=True)
    hostname = Column(String)
    ip = Column(String)
    memory = Column(Integer)
    active = Column(Boolean)

res = Resource(hostname="rjekker.nl",\
                     ip="123.456.7.8",\
                 memory=50000,\
                 active=True)

Base.metadata.create_all(engine)