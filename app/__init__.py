from flask import Flask
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from flask_debugtoolbar import DebugToolbarExtension
import better_exceptions
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
app.config.from_pyfile('config.py')

from app.util.filters import blueprint
app.register_blueprint(blueprint)

toolbar = DebugToolbarExtension(app)

dbPath = 'mysql+mysqlconnector://root@localhost/'
admin_db = 'information_schema'
working_db = 'project_db'

Base = declarative_base()

admin_engine = create_engine(dbPath + admin_db, echo=True)
admin_metadata = MetaData(admin_engine)

engine = create_engine(dbPath + working_db)
conn = engine.connect()
metadata = MetaData(engine, reflect=True)

from app import views, models
