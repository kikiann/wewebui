from flask import Flask
import os

app = Flask (__name__)
@app.route('/skills')
def skills():
    #read the skills list from file
    fileName = 'static/skills.csv'
    skillsList = readFile(fileName)
    bookings()
    return render_template('skills.html',skillsList=skillsList)

def get_last_row(csv_filename):
    with open(diff_file.csv, 'r') as f:
        lastrow = None
        for lastrow in csv.reader(f): pass
        return lastrow

def bookings():
    file = 'static/skills.csv'
    check = False
    isBooked = get_last_row(file)
    if isBooked == 'booked':
        check = True