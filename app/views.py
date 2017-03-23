from flask import render_template, request,flash, redirect, url_for
from app import app, db
from app.models import Changes

@app.route('/' , methods=['GET'])
def changelog():
    if request.method == 'GET':
        changes = Changes.query.all()
    return render_template('changelog.html', changes=changes)
