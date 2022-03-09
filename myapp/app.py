from flask import Flask, render_template, request 
app = Flask(__name__)

# 크롤링 라이브러리
import requests
from bs4 import BeautifulSoup

@app.route('/')
def hello():
    return render_template("hello.html")


@app.route('/apply')
def apply():
    return render_template('apply.html')


@app.route('/applyphoto', methods = ['POST', 'GET'])
def applyPhoto():
    
    if request.method == 'GET':
        val = request.args.get('location')
        val2 = request.args.get('introduce')
        return render_template('applyphoto.html', location=val, introduce=val2)


    # location = request.args.get("location")
    # photo = request.args.get("clean")
    # introduce = request.args.get("introduce")
    # print(location, photo, introduce)
    # return render_template('applyphoto.html')


@app.route('/list')
def list():
    return render_template('list.html')


if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0', port=5050)
