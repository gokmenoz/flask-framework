from flask import Flask,render_template,request
import os
import requests
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components

link_start='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
link_end='&outputsize=full&apikey=R2QQ29L68BZH01JJ'

def graph(sym,yr,month):
    response=requests.get(link_start+sym+link_end)
    data=response.json()['Time Series (Daily)']

    df=pd.DataFrame(data)
    df=df[[col for col in df.columns if col[0:4]==yr and col[5:7]==month]]
    df=df[df.index=='4. close']
    df=df.T
    
    p = figure(plot_width=600, plot_height=400)
    x_axis=[i for i in range(len(df.values))]
    p.line(x_axis,df['4. close'].iloc[::-1], line_width=2)
    output_file('image.html')
    show(p)

app = Flask(__name__)

@app.route('/')
def index_lulu():
    return render_template('stockticker.html')
    
@app.route('/static/<path:path>',methods=['GET','POST'])
def static_file(path):
    return app.send_static_file(os.path.join('static', path))

@app.route('/stockticker.html',methods=['GET','POST'])
def hello1():
    return render_template('stockticker.html')

@app.route('/image.html',methods=['GET','POST'])
def hello3():
    symbol=request.form['symbol_lulu']
    year=request.form['year_lulu']
    month=request.form['month_lulu']
    graph(symbol,year,month)
    return render_template('image.html')
        
@app.route('/stock.html',methods=['GET','POST'])
def hello2():
    symbol=request.form['symbol_lulu']
    year=request.form['year_lulu']
    month=request.form['month_lulu']
    return render_template('stock.html',symbol=symbol,year=year,month=month,div=graph(symbol,year,month)[0],script=graph(symbol,year,month)[1])
    
if __name__ == "__main__":
    app.run(debug=False)
