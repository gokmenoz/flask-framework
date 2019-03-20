from flask import Flask,render_template,request
import os
import requests
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import Range1d

link_start='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
link_end='&outputsize=full&apikey=R2QQ29L68BZH01JJ'
company_list=pd.read_table('static/NASDAQ.txt')


def start_year_finder(df):
    return df.columns[-1][0:4]
    
def get_data(sym):
    response=requests.get(link_start+sym+link_end)
    data=response.json()['Time Series (Daily)']
    return pd.DataFrame(data)
    
def graph(df,yr,month,price):
    df=df[[col for col in df.columns if col[0:4]==yr and col[5:7]==month]]
    df=df[df.index==price]
    df=df.T
    
    p = figure(plot_width=600, plot_height=400, x_axis_label='Day',y_axis_label='Price')
    x_axis=[i for i in range(1,len(df.values)+1)]
    p.line(x_axis,df[price].iloc[::-1], line_width=2)
    p.y_range=Range1d(min(df[price].astype(float)),max(df[price].astype(float)))
    return components(p)

app = Flask(__name__)

@app.route('/')
def index_lulu():
    return render_template('stockticker.html')
    
@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(os.path.join('static', path))

@app.route('/stock.html',methods=['POST'])
def hello2():
    symbol=request.form['symbol_lulu']
    year=request.form['year_lulu']
    month=request.form['month_lulu']
    price=request.form['type_lulu']
    df=get_data(symbol)
    years=[str(i) for i in range(int(start_year_finder(df)),2020)]
    if symbol not in company_list['Symbol'].values:
        return 'Please enter a valid stock symbol'
    elif year not in years:
        return 'There is no data for this year'
    elif year=='2019' and int(month)>3:
        return 'Please enter a date before Apr 2019'
    else:
        script,div=graph(df,year,month,price)
        return render_template('stock.html',company=list(company_list[company_list['Symbol']==symbol]['Description'])[0],year=year,month=month,div=div,script=script,price=price)
    
if __name__ == "__main__":
    app.run(debug=False)
