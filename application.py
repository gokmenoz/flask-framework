from flask import Flask,render_template,request
import os

app = Flask(__name__)

@app.route('/')
def index_lulu():
    return render_template('ZUMZ.html')
    
@app.route('/static/<path:path>',methods=['GET','POST'])
def static_file(path):
    return app.send_static_file(os.path.join('static', path))

@app.route('/stockticker.html',methods=['GET','POST'])
def hello1():
    return render_template('stockticker.html')
        
@app.route('/stock.html',methods=['GET','POST'])
def hello2():
    return render_template('stock.html',symbol=request.form['symbol_lulu'],month=request.form['month_lulu'])
    
if __name__ == "__main__":
    app.run(debug=False)
