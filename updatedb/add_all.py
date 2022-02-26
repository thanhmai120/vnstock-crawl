# from models import Stock, Change
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///vnstock.db', echo=False)

# add all stocks
all_stocks = pd.read_csv('vnstock_data/all_stock.csv')
all_stocks = all_stocks.drop_duplicates(subset=['code'])
all_stocks.to_sql('stocks', con=engine, if_exists='append', index=False)

# add all changes
for idx, stock in all_stocks.iterrows():
    try:
        stock_changes = pd.read_csv('vnstock_data/' + str(stock['code']) + '.csv')
    except:
        continue
    stock_changes['code'] = stock['code']
    stock_changes.to_sql('changes',con=engine, if_exists='append', index=False)