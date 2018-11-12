#/usr/bin/env python3
from dbutils import db_connect
import sqlite3
import os
import sys
conn = db_connect("db_router.sqlite3")
#CREATE TABLE 
inv_table_sql = '''CREATE TABLE INVENTORY
         (IP TEXT PRIMARY KEY     NOT NULL,
          LOCATION         CHAR(50)    NOT NULL,
          BRAND            TEXT        NOT NULL,
          USERNAME         CHAR(20),
          PASSWORD         CHAR(20));'''
try:
    conn.execute(inv_table_sql)
except sqlite3.OperationalError:
    print("Can't create Table!")
    sys.exit(1)
print("Table INVENTORY created successfully")

#print table
for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table';"):
    print(row)


 