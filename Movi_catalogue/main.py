from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = ["Matrix", "7", "Forest"]
    return render_template("homepage.html", movies=movies)