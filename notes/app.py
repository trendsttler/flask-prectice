from flask import Flask, render_template, request, session
from flask_session import session
 
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config{"session_type"} = "filesystem"
ession(app)

notes = []

@app.route("/", methodes=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("index.html" notes=note)