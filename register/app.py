from flask import Flask, render_template, request

app = Flask(__name__)

  
@app.route("/")
def index():
     return render_template("register.html")

@app.route("/user_profile", methods=['GET','POST'])
def profile():
    if request.method == "GET":
        return "Please Sign up First"
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        return render_template("user.html", name=name, email=email, password=password)  
      