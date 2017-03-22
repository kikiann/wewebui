from flask import Flask
import os

app = Flask (__name__)

#fun var

filepath = os.path.join(os.path.dirname(__file__),'diff_file.csv')

open_read = open(filepath,'r')
page =''

while True:
    read_data = open_read.readline()
    page += '<p>%s</p>' % read_data
    if open_read.readline() == '':
        break

@app.route("/")
def index():
    return page


if __name__ == "__main__":
    app.run()