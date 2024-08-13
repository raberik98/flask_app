from flask import Flask, request, render_template
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=["GET"])
def index():
    content = [ "Introduction", "Shop", "Cart" ]
    
    return render_template("home.html",
                           title="Home",
                           content=content
                           )


@app.template_filter("reverse_string")
def reverse_string(text):
    return text[::-1]


@app.template_filter("repeate")
def repeate(text, times=2):
    return text * times


@app.route("/filters", methods=["GET"])
def filters():
    content = ["one", "two", "three", "four"]

    return render_template("filters.html",
                           title="Filters",
                           content=content
                           )

if __name__ == '__main__':
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=True)