from typing import Text
from flask import Flask
from flask import render_template
from jinja2 import Template
import os
from get_data import get_posts

app = Flask(__name__)

@app.route("/")
def home_page():
    posts = get_posts()
    peaked = posts[0]
    stream = posts[1]
    tvt = posts[2]
    consolidated = posts[3]
    news = posts[4]
    return render_template("index.html", peaked=peaked, stream=stream, tvt=tvt, consolidated=consolidated, news=news)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888)