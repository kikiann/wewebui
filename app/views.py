from flask import render_template, request,flash, redirect, url_for
from app import app, working_db
from app.models import Changes, Tables, session
import better_exceptions

@app.route('/')
def changelog():
    all_tables = session.query(Tables).filter(Tables.table_schema == working_db)
    return render_template('changelog.html', all_tables=all_tables, database = working_db)
