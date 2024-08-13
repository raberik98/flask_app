from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"


@app.route("/hi/<name>")
def name(name):
    return f"<h2>Hello {name}<h2>"


@app.route("/add/<int:number1>/<int:number2>")
def add(number1, number2):
    return f"<h1>The value is: {number1 + number2}</h1>"


@app.route("/queries")
def queries():
    if "data" in request.args.keys() and "data2" in request.args.keys():
        data = request.args.get('data')
        data2 = request.args['data2']
        return f"first: {data} and second: {data2}"
    else: 
        return "<h1>Error give some deceant data!</h1>"


if __name__ == '__main__':
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=True)