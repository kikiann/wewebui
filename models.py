from app import metadata, admin_metadata, admin_engine, conn
from sqlalchemy import Table, Column, String, select
from sqlalchemy.orm import mapper, sessionmaker, clear_mappers

class Tables(object):
    pass

def get_tables(db):
    clear_mappers()
    tables = Table('tables', admin_metadata,
                        Column('table_catalog', String, primary_key=True),
                        Column('table_schema', String),
                        Column('table_name', String),
                        autoload=True, extend_existing=True)
    mapper(Tables, tables)
    Session = sessionmaker(bind=admin_engine)
    session = Session()

    res = session.query(Tables).filter(Tables.table_schema==db)
    return res

def get_entries(table):
    tbl_name = metadata.tables[table]
    query = tbl_name.select(tbl_name)
    return conn.execute(query)