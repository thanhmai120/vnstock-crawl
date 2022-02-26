from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine =  create_engine('sqlite:///vnstock.db', echo=False)
Session = sessionmaker(engine)
session = Session()
Base = declarative_base()

class Stock(Base):
    __tablename__  = "stocks"
    code = Column(String, primary_key=True)
    floor = Column(String)
    isin = Column(String)
    company = Column(String)
    companyId = Column(Integer)
    listedDate = Column(Date) 
    changes = relationship("Change", backref="stocks")

class Change(Base):
    __tablename__ = "changes"
    date = Column(Date, primary_key=True)
    close = Column(Numeric)
    open = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    change = Column(Numeric)
    code = Column(String, ForeignKey("stocks.code"))

rs = session.query(Stock).count()
print(rs)