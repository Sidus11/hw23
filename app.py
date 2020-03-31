from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/lst")
def lst():
    return render_template("lst.html")

@app.route("/rec")
@app.route("/rec/<string:man>")
def rec(man = ""):
    return render_template("rec.html", man = man)