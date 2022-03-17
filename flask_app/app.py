import os
from flask import Flask, render_template, request, url_for,  redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "sdliwoguihaq3l56ksga"

# 아이디랑 비밀번호 sqlite로 만들어보기

# @app.route('/')
# def hello():
#     return render_template("hello.html")

@app.route("/")
def home():
    if "userID" in session: #로그인 된 상태
        return render_template("home.html", username = session.get("userID"), login = True) # 세션에 있는 userId를 가져온다.
    else:
        return render_template("home.html", login = False)

    #return render_template("login.html")


@app.route("/login", methods= ["get"])
def login():
    global ID, PW
    _id_ = request.args.get("loginId")
    _password_ = request.args.get("loginPw")

    if ID == _id_ and PW == _password_:
        print(_id_, _password_)
        session["userID"] = _id_
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session.pop("userID")
    return redirect(url_for("home"))

@app.route('/apply')
def apply():
    return render_template('apply.html')


@app.route('/applyphoto', methods = ['POST', 'GET'])
def applyPhoto():
    
    if request.method == 'GET':
        val = request.args.get('location')
        val2 = request.args.get('introduce')
        return render_template('applyphoto.html', location=val, introduce=val2)

@app.route('/list')
def list():
    return render_template('list.html')


if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0', port=5050)
