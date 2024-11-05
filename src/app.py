from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/walper")
def walper():
    return render_template("walper.html")

@app.route("/walperpedia")  
def WalperPedia():
    return render_template("WalperPedia.html")

app.run(host="0.0.0.0", debug=True)