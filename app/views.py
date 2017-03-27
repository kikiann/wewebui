from flask import render_template, request,flash, redirect, url_for
from app import app, working_db
from app.models import get_tables, get_entries
import better_exceptions
import sys

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
def tbl_selector():
    _tbl = request.args.get('tbl')
    if not _tbl == None:
        all_entries = get_entries(_tbl)
        return render_template('changelog.html', all_entries=all_entries)
    else:
        return page_not_found()
