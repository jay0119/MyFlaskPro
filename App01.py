from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/math', methods=["POST"])
def calculate():
    print(str(request.form))
    operation = request.form["operation"]
    num1 = int(request.form["num1"])
    num2 = int(request.form["num2"])
    if operation== "add":
        result = num1 + num2
        addResult =f"Sum of {num1} + {num2} is {result}"
    elif operation== "subtract":
        result = abs(num1 - num2)
        addResult =f"Subtraction of {num1} - {num2} is {result}"
    elif operation== "multiply":
        result = num1 * num2
        addResult =f"Multiplication of {num1} * {num2} is {result}"
    elif operation== "divide":
        result = num1 / num2
        addResult =f"Division of {num1} / {num2} is {result}"
    else:
        addResult =f"{operation} is either not arithmatic or its not supported."
    return render_template('results.html',result = addResult)


if __name__ == "_main_":
  app.run(host="0.0.0.0")