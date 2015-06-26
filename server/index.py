import flask
from flask import request

app=flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])

def index():
    if flask.request.method == 'POST': 
        print('receive a post')
        data=request.json
        print(data['value'])

    return 'hello im index'

@app.route('/hello/')
@app.route('/hello/<name>')

def hello(name=None):
    return flask.render_template('hello.html',name=name)



if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')
