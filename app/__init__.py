from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
import better_exceptions

app = Flask(__name__)
app.config.from_object('config')

dbPath = 'mysql+mysqlconnector://root@localhost/'
admin_db = 'information_schema'
working_db = 'project_db'

Base = declarative_base()

admin_engine = create_engine(dbPath + admin_db, echo=True)
admin_metadata = MetaData(admin_engine)

engine = create_engine(dbPath + working_db, echo=True)
metadata = MetaData(bind=engine)

from app import views, models
