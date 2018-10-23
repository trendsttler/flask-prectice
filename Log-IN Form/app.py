from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user", methods=["GET", "POST"])
def user():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template("user.html", name=name, email=email, password=password)
