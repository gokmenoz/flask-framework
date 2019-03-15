from flask import Flask,render_template
import os

app = Flask(__name__)

@app.route('/')
def index_lulu():
    return render_template('ZUMZ.html')
    
@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(os.path.join('static', path))

@app.route('/ZQK.html')
def hello1():
    return render_template('ZQK.html')

@app.route('/ZTS.html')
def hello2():
    return render_template('ZTS.html')

if __name__ == "__main__":
    app.run(debug=False)
