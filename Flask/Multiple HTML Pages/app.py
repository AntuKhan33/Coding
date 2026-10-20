from flask import Flask,render_template

app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/first")
def first():
    return render_template("first_page.html")

@app.route("/second")
def second():
    return render_template("second_page.html")

if __name__=="__main__":
    app.run(debug=True)