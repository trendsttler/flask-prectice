from flask import Flask, render_template 

app = Flask(__name__)
 
@app.route("/")
def name():
   names = ["alice","rony","lavisha"]
   return render_template("loop.html", names=names)  