#!/usr/bin/env python
# Please update inventory.csv for IP and Credentials
import csv
import sys
import paramiko
import time
import re
import ipaddress
success = 0
failure = 0
iteration = 0
inventory_file = input("Please input the path of CSV file (Ex: D:\inventory.csv): ")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    f = open(inventory_file,"r")
except : 
    print("Error Opening {}. Please recheck!".format(inventory_file))
    sys.exit(1)
csv_content = csv.DictReader(f)
for row in csv_content:
    iteration += 1
    #print(row["Name"],row["IP"],row["Username"],row["Password"])
    try:
        ipaddress.ip_address(row["IP"])
    except ValueError:
        print("Invalid IP Address Format : {} --> Please check IP Address on row number {}!".format(row["IP"],iteration))
        failure += 1
        continue
    device_info = { "ip": row["IP"],
                    "username":row["Username"],
                    "password":row["Password"],
                  }
    #print(device_info)    
    try:
        ssh_client.connect(device_info["ip"],username=device_info["username"],password=device_info["password"])
    except:
        print("SSH Connection Error for {}. Please check your connection or credentials!".format(device_info["ip"]))
        failure += 1
        continue
    print("Successfully connect to {}".format(device_info["ip"]))
    success += 1
    ssh_conn = ssh_client.invoke_shell()
    ssh_conn.send("terminal length 0\n")
    ssh_conn.send("show run")
    ssh_conn.send("\n")
    time.sleep(2)
    if ssh_conn.recv_ready():
        output = ssh_conn.recv(65535)
    # Python3 treat default to binary raw bits, not string implicitly --> use .decode()
    output_str=str(output.decode())
    output_str = re.search(r"!.*end",output_str,flags=re.DOTALL).group(0)
    with open("{}.cfg".format(device_info["ip"]), mode="w") as f:
        f.write(output_str)
    print("Successfully backup device {}".format(device_info["ip"])) 
f.close()
print("Attempt to backup {} devices".format(success+failure))
print("Success : {}".format(success))
print("Failure : {}".format(failure))


