from importlib.resources import contents
from unicodedata import name
from flask import Flask, redirect, url_for
from flask import Flask, render_template
app = Flask(__name__)



@app.route("/<name>")
def home(name):
    return render_template("index.html",content=['time','jim'])




# @app.route("/")
# def home():
#     return" hello this is main page <h1>hello</h1>"

# @app.route("/<name>")
# def  user(name):
#     return f"hello{name}  ! "    


# @app.route("/admin")
# def admin():
#     return redirect(url_for("user",name="Admin"))




if __name__ == "__main__":
	app.run(debug = True)
 
 
