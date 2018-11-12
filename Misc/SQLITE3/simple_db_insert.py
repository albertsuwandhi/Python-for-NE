#/usr/bin/env python3
from dbutils import db_connect
import sqlite3
import os
import sys
conn = db_connect("db_router.sqlite3")
#INSERT VALUE into TABLE
try:
    conn.execute("INSERT INTO INVENTORY (IP,LOCATION,BRAND,USERNAME,PASSWORD) VALUES ('10.10.10.10', 'Medan', 'Cisco', 'admin', 'admin')")
    conn.execute("INSERT INTO INVENTORY (IP,LOCATION,BRAND,USERNAME,PASSWORD) VALUES ('10.10.10.20', 'Medan', 'Juniper', 'admin', 'admin123')")
    conn.execute("INSERT INTO INVENTORY (IP,LOCATION,BRAND,USERNAME,PASSWORD) VALUES ('10.10.10.30', 'Medan', 'Brocade', 'admin', 'admin321')")
    conn.execute("INSERT INTO INVENTORY (IP,LOCATION,BRAND,USERNAME,PASSWORD) VALUES ('10.10.10.40', 'Jakarta', 'HuaWei', 'huawei', 'china')")
    conn.commit()
except:
    print("Can't Insert Records into INVENTORY Table")
    sys.exit(1)
print ("Records created successfully")
#SELECT and print the records
try:
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
    




 