from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData

app = Flask(__name__)
app.config.from_object('config')

#db = SQLAlchemy(app)

dbPath = 'mysql+pymysql://root@localhost/'

admin_engine = create_engine(dbPath + 'information_schema', echo=True)
admin_metadata = MetaData(admin_engine)

engine = create_engine(dbPath + 'project_db', echo=True)
metadata = MetaData(engine)

from app import views, models
