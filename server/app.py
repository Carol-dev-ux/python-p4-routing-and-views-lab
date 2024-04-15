#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:input_string>')
def print_string(input_string):
    print(input_string)  # Print the string to the console
    return f'<h2>String printed: {input_string}</h2>'  # Display the string in the web browser

@app.route('/count/<int:num>')
def count(num):
    numbers = '<br>'.join(str(i) for i in range(1, num+1))
    return f'<h2>Counting from 1 to {num}:</h2><p>{numbers}</p>'

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<h2>Error: Division by zero</h2>'
    elif operation == '%':
        result = num1 % num2
    
    if result is not None:
        return f'<h2>Result of {num1} {operation} {num2}: {result}</h2>'
    else:
        return '<h2>Error: Invalid operation</h2>'

if __name__ == '__main__':
    app.run(debug=True)
