from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename
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

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "GET":
        return render_template("profile.html")
    else:
        return f"{request.form.get('name')}"


@app.route("/file", methods=["GET","POST"])
def upload():
    if request.method == "GET":
        return render_template("file.html")
    else:
        if "img" not in request.files:
            return 'No file provided'
        
        file = request.files['img']

        if file.filename == '':
            return 'No selected file'
        
        if file:
            secure_name = secure_filename(file.filename)

            file.save(f'./uploads/{secure_name}',)
            return 'Success!'
        else:
            return 'Failure!'


if __name__ == '__main__':
    app.run(host=os.getenv("HOST"), port=os.getenv("PORT"), debug=True)