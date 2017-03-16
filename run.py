# Python libs

# 3rd party libs
from flask import Flask, render_template

# My libs

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def index():

    return render_template('index.html')
