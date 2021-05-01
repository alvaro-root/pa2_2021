from sqlalchemy import create_engine
import getpass

DB_DEFAULTS = {
    "host": "localhost",
    "port": 25432,
    "database": "gis",
    "userid": "docker",
}


host = input(f"Host: (ENTER for 'localhost')") or DB_DEFAULTS["host"]
port = input(f"Port: (ENTER for 25432)") or f'{DB_DEFAULTS["port"]}'
database = input(f"Database: (ENTER for 'gis')") or DB_DEFAULTS["database"]
uid = input(f"UserId: (ENTER for 'docker')") or DB_DEFAULTS["userid"]
pwd = getpass.getpass()
db_connection = f"postgresql://{uid}:{pwd}@{host}:{port}/{database}"

try:
    engine = create_engine(db_connection)
    # connection = engine.connect()
except Exception as e:
    print(f"{e}")
    quit(1)