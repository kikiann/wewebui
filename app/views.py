from flask import render_template, request, flash, redirect, url_for
from app import app, working_db
from app.models import get_tables, get_entries
import better_exceptions
import os

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route('/')
def home():
    return render_template('changelog.html', database = working_db)

@app.route('/<db>')
def db_selector(db):
    all_tables = get_tables(db)
    return render_template('changelog.html', all_tables=all_tables, database=db)

@app.route('/<db>/table')
def tbl_selector(db):
    _tbl = request.args.get('tbl')
    if not _tbl == None:
        all_tables = get_tables(db)
        all_entries = get_entries(_tbl)
        return render_template('changelog.html', database=db, all_tables=all_tables, all_entries=all_entries)
    else:
        return page_not_found()

@app.route('/contents')
def view_contents():
    filepath = request.args.get('filepath')
    if filepath:
        with open(filepath) as f:
            lines = f.readlines()
        list_lines = []
        for line in lines:
            list_lines.append(line.replace("\n", ""))
        content = '\n'.join(map(str, list_lines))
        return render_template('contents.html', content=content)
    else:
        return page_not_found()


@app.route('/contents/accept')
def accept():
     f = open("attendedfile.txt", "w")
     tempfile =
for tempfile in tempfiles:
    f.write(tempfile.read())

@app.route('/contents/reject')
def reject():
     f = open("unattendedfile.txt", "w")
for tempfile in tempfiles:
    f.write(tempfile.read())
