from flask import render_template, request,flash, redirect, url_for
from app import app#, db
from app.models import Changes, master_table, loadSession

@app.route('/')
def changelog():
    session = loadSession()
    all_tables = session.query(master_table).all()
    return render_template('changelog.html', all_tables=all_tables)
