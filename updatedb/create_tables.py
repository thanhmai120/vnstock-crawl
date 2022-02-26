from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, Numeric, ForeignKey

engine = create_engine('sqlite:///vnstock.db', echo=False)
meta = MetaData()

stocks = Table(
   'stocks', meta, 
   Column('code', String, primary_key = True), 
   Column('floor', String), 
   Column('isin', String), 
   Column('company', String),
   Column('listedDate', String),
   Column('companyId', Integer),
)

changes = Table(
   'changes', meta, 
   Column('date', Date, primary_key = True), 
   Column('close', Numeric),  
   Column('open', Numeric),  
   Column('high', Numeric),  
   Column('low', Numeric),  
   Column('change', Numeric), 
   Column('volume',Numeric),
   Column('code', String, ForeignKey("stocks.code"), primary_key = True),
)

meta.drop_all(engine)
meta.create_all(engine)