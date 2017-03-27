from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from flask_debugtoolbar import DebugToolbarExtension
import better_exceptions

app = Flask(__name__)
app.config.from_object('config')

toolbar = DebugToolbarExtension(app)

dbPath = 'mysql+pymysql://root@localhost/'
admin_db = 'information_schema'
working_db = 'project_db'

#Base = declarative_base()

admin_engine = create_engine(dbPath + admin_db)
admin_conn = admin_engine.connect()
admin_metadata = MetaData(admin_engine, reflect=True)

engine = create_engine(dbPath + working_db)
conn = engine.connect()
metadata = MetaData(engine, reflect=True)

from app import views, models
