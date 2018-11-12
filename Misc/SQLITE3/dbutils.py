import sqlite3
import os
import sys
DEFAULT_PATH = os.path.join(os.path.dirname(__file__),"db.sqlite3")
def db_connect(db_path=DEFAULT_PATH):
    try:
        conn = sqlite3.connect(db_path)
    except:
        print("Cannot connect to database : {}".format(db_path))
        sys.exit(1)
    print("Connected to {}".format(db_path))
    print("-"*50)
    return conn
