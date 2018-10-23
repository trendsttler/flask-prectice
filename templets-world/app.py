from flask import Flask, render_template 

app = Flask(__name__)

  
@app.route('/')
def index():
    return "heloo"

@app.route('/<string:name>')
def hello(name):
    title = name
    return render_template("index.html", title=title)  
      