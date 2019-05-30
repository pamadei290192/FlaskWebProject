from flask import Flask,render_template
from HelloFlask import app
import datetime as dt

@app.route('/')
@app.route('/home')

def home():
    now = dt.datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return render_template(
        "index.html",
        title = "Hello Flask",
        message = "Hello, Flask!",
        content = " on " + formatted_now)