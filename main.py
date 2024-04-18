#osnovna struktura za flask app

#PIP ORODJE
from flask import Flask, render_template

#new object "app"
app = Flask(__name__)


# root of  the page/app - controller
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == '__main__':
    app.run(use_reloader=True)