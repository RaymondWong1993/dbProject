from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import *

## dialect+driver://username:password@host:port/database
__db_path = DB_DIALECT + DB_DRIVER + r'://' + DB_USERNAME + r':' + \
    DB_PASSWORD + r'@' + DB_HOST + r':' + DB_PORT + r'/' + DB_DATABASE + DB_QUERYSTRING

_conn = None
_session = None

def initDb():
    engine = create_engine(__db_path)
    _conn = engine.connect()
    Session = sessionmaker()
    Session.configure(bind=_conn)
    _session = Session()
    return (_conn, _session)

def closeDb():
    if _conn and _session:
        _session.close()
        _conn.close()
