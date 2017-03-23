from app import admin_engine, engine, admin_metadata, metadata
from sqlalchemy import Table, Column, BigInteger, String
from sqlalchemy.orm import mapper, sessionmaker

class Changes():
    pass

class master_table(object):
    pass

# get all table names in project_db from information_schema.tables
def loadSession():
    information_schema = Table('tables', admin_metadata,
                                Column("table_catalog", String, primary_key=True),
                                autoload=True)
    mapper(master_table, information_schema)
    Session = sessionmaker(bind=admin_engine)
    session = Session()
    return session

session = loadSession()
