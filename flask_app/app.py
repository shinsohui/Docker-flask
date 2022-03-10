from flask import Flask, render_template, request 
app = Flask(__name__)

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

@app.route('/list')
def list():
    return render_template('list.html')


if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0', port=5050)
