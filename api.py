from flask import Flask,jsonify,request
app=Flask(__name__)
from data import data

@app.route('/')
def index():
    return jsonify({
        'data':data,
        'message':'success',
    }),200

@app.route('/stars')
def stars():
    name=request.args.get('name')
    star_data=next(i for i in data if i['name']==name)
    return jsonify({
        'data':star_data,
        'message':'success',
    }),200

if __name__=='__main__':
    app.run()
