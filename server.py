from flask import Flask, request, render_template
from mathematics import Maths


app = Flask('Mathematics Problem Solver')


@app.route('/')
def render_index_page():
    return render_template('index.html')


@app.route('/sum')
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = Maths.summation(num1, num2)
    return str(result), 200


@app.route('/sub')
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = Maths.subtraction(num1, num2)
    return str(result), 200


@app.route('/mul')
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = Maths.multiplication(num1, num2)
    return str(result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
