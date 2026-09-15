#imp
from flask import Flask, render_template
#Imports Flask, the class we use to create our web application.
app = Flask(__name__)

#create app & store in app
@app.route("/")
def home():
    return render_template("index.html")
#handles requests for / (the home page) and returns a simple HTML

if __name__ == "__main__":
    app.run(port=5001, debug=True)