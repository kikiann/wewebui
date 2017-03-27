from app import metadata, admin_metadata, conn, admin_conn
from sqlalchemy import Table, Column, String, select

def get_tables(db):
    tbl_name = admin_metadata.tables['TABLES']
    dump(admin_metadata)
    query = tbl_name.select(tbl_name.c.table_name).where(table.c.table_schema == db)
    return admin_conn.execute(query)

def get_entries(table):
    tbl_name = metadata.tables[table]
    query = tbl_name.select(tbl_name)
    return conn.execute(query)
