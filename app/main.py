from flask import Flask, request
# from flask_ngrok import run_with_ngrok
import json
import pandas as pd

app = Flask(__name__)
# run_with_ngrok(app)
  
@app.route("/crawlstockchange",methods=['GET', 'POST'])
def crawl_change():
    if request.method == 'POST':
        json_data:dict = json.loads(str(request.data.decode('utf-8')))
        for key,val in json_data.items():
            code = key
            data = val
            df = pd.DataFrame(data)
            if 'Date' in df:
                df['Date'] = pd.to_datetime(df['Date'])
            df.to_csv('vnstock_data/'+code+'.csv',index=False)
            # with open('vnstock_data/'+code+'.json','w',encoding="utf-8") as out_file:
            #     out_file.write(str(data))
    return ('successfully crawl '+code)

@app.route("/crawlstock",methods=['GET', 'POST'])
def crawl_stock():
    if request.method == 'POST':
        json_data:dict = json.loads(str(request.data.decode('utf-8')))
        data = json_data.get('data')
        df = pd.DataFrame(data)
        df = df[['code','floor','isin','companyNameEng','listedDate','companyId']]
        df = df.rename(columns={'companyNameEng':'company'})
        df['listedDate'] = pd.to_datetime(df['listedDate'])
        df.to_csv('vnstock_data/all_stock.csv', index=False)
    return ('successfully crawl all stocks')

@app.route("/updatedb",methods=['GET', 'POST'])
def update_db():
    if request.method == 'POST':
        import updatedb
        return('updated db')
