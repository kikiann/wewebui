from flask import render_template, request,flash, redirect, url_for
from app import app, working_db
from app.models import Tables, admin_session, session
import better_exceptions

global all_tables

@app.route('/')
def home():
    return render_template('changelog.html', database = working_db)

@app.route('/<db>')
def changelog(db):
    all_tables = admin_session.query(Tables).filter(Tables.table_schema == db)
    return render_template('changelog.html', all_tables=all_tables, database = db)
