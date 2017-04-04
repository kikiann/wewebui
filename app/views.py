from flask import render_template, request, flash, redirect, url_for
from app import app, working_db
from app.models import get_tables, get_entries
import better_exceptions
import logging, traceback

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
        return render_template('contents.html', content=content, filepath=filepath)
    else:
        return page_not_found()


@app.route('/contents/accept')
def accept():
    filepath = request.args.get('filepath')
    if filepath:
        try:
            with open("output\\attendedfile.txt", "a") as dst_f:
                with open(filepath, "r") as src_f:
                    dst_f.write(src_f.read())
            return render_template('process.html', comment="Success.")
        except Exception as e:
            logging.error(traceback.format_exc())
    else:
        return render_template('process.html', comment="Failed. Check server console log for error details.")
        return page_not_found()


@app.route('/contents/reject')
def reject():
    filepath = request.args.get('filepath')
    if filepath:
        try:
            with open("output\\unattendedfile.txt", "a") as dst_f:
                with open(filepath, "r") as src_f:
                    dst_f.write(src_f.read())
            return render_template('process.html', comment="Success.")
        except Exception as e:
            logging.error(traceback.format_exc())
            return render_template('process.html', comment="Failed. Check server console log for error details.")
    else:
        return page_not_found()
