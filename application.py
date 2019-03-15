from flask import Flask,render_template,request
import os

app = Flask(__name__)

@app.route('/')
def index_lulu():
    return render_template('ZUMZ.html')
    
@app.route('/static/<path:path>',methods=['GET','POST'])
def static_file(path):
    return app.send_static_file(os.path.join('static', path))

@app.route('/ZQK.html',methods=['GET','POST'])
def hello1():
    if request.method=='GET':
        return render_template('ZQK.html',ticker='ZQK')
    else:
        return request.form['name_lulu']+request.form['age_lulu']
    
@app.route('/ZTS.html',methods=['GET','POST'])
def hello2():
    if request.method=='GET':
        return render_template('ZTS.html')
    else:
        return render_template('ZTS.html',name=request.form['name_lulu'],age=request.form['age_lulu'])

if __name__ == "__main__":
    app.run(debug=False)
