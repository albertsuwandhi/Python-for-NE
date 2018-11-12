#/usr/bin/env python3
from dbutils import db_connect
import sqlite3
import os
import sys
conn = db_connect("db_router.sqlite3")
#SELECT and print the records
try:
    print("Query INVENTORY Table and print the results")
    print("-"*50)
    cursor = conn.execute("SELECT IP, LOCATION, BRAND, USERNAME, PASSWORD from INVENTORY")
    for row in cursor:
        print ("IP = ", row[0])
        print ("LOCATION = ", row[1])
        print ("BRAND = ", row[2])
        print ("USERNAME = ", row[3])
        print ("PASSWORD = ", row[4])
        print("-"*50)
except:
    print("Can't not get records form INVENTORY Table")
    sys.exit(1)

#UPDATE and print the records
print("Update INVENTORY Table and print the results")
print("-"*50)
cursor = conn.execute('UPDATE INVENTORY set PASSWORD = "Secret@12345" where BRAND = "Juniper"')
conn.commit()
print("{} row(s) updated".format(conn.total_changes))
print("-"*50)
cursor = conn.execute("SELECT IP, LOCATION, BRAND, USERNAME, PASSWORD from INVENTORY")
for row in cursor:
    print ("IP = ", row[0])
    print ("LOCATION = ", row[1])
    print ("BRAND = ", row[2])
    print ("USERNAME = ", row[3])
    print ("PASSWORD = ", row[4])
    print("-"*50)
conn.close()

#DELETE and print the records
conn = db_connect("db_router.sqlite3")
print("Delete some record(s) from INVENTORY Table and print the results")
print("-"*50)
cursor = conn.execute('DELETE from INVENTORY where BRAND = "Juniper"')
conn.commit()
print("{} row(s) updated".format(conn.total_changes))
print("-"*50)
cursor = conn.execute("SELECT IP, LOCATION, BRAND, USERNAME, PASSWORD from INVENTORY")
for row in cursor:
    print ("IP = ", row[0])
    print ("LOCATION = ", row[1])
    print ("BRAND = ", row[2])
    print ("USERNAME = ", row[3])
    print ("PASSWORD = ", row[4])
    print("-"*50)
conn.close()

    




 