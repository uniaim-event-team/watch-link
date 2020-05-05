from flask import Blueprint, render_template

app = Blueprint(__name__, "server")


@app.route('/')
def route():
    return render_template('top.html')
