# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_nums():
    """Add a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)

@app.route("/sub")
def sub_nums():
    """subtract a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)

    return str(result)

@app.route("/mult")
def mult_nums():
    """multiply a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)

@app.route("/div")
def div_nums():
    """divide a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
    }

@app.route("/math/<oper>")
def do_math(oper):
    """Perform entered operation on a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a,b)

    return result