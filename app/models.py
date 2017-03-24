from app import engine, metadata, admin_engine, admin_metadata, Base
from sqlalchemy import Table, Column, BigInteger, String
from sqlalchemy.orm import mapper, create_session

class Changes():
    pass

class Tables(Base):
    __table__ = Table('tables', Base.metadata,
                        Column("table_catalog", String, primary_key=True),
                        Column("table_schema", String),
                        Column("table_name", String),
                        autoload=True, autoload_with=admin_engine)

    def __repr__(self):
        return self.table_name

def loadSession():
    session = create_session(bind=admin_engine)
    return session

session = loadSession()
