# -*- coding: utf-8 -*-
from flask import Flask
import taglib
import os

app = Flask (__name__)

#fun var

dataset = taglib.Dataset()
with open(os.path.join('diff_file.csv'))as f:
    dataset.csv = f.read()


@app.route("/")
def index():
    return dataset.html


if __name__ == "__main__":
    app.run()