#!/usr/bin/env python3
# -- Written by : Albert -----
import paramiko
import time
import re
import sys
from getpass import getpass
print("--- Backup Switch Config  ---")
my_devices = ['192.168.160.131', '192.168.160.132']
username = input("Please enter username  : ")
password = getpass("Please enter password: ")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for ip in my_devices:
    try:
        ssh_client.connect(ip,username=username,password=password)
    except:
        print("SSH Connection Error!! Please check your connection and credentials! ")
        sys.exit(1)
    print(f"Successfully connect to {ip}")
    ssh_conn = ssh_client.invoke_shell()
    ssh_conn.send("terminal length 0\n")
    ssh_conn.send("show run")
    ssh_conn.send("\n")
    time.sleep(2)
    if ssh_conn.recv_ready():
        output = ssh_conn.recv(65535)
    Python3 treat default to binary raw bits, not string implicitly --> use .decode()
    output_str=str(output.decode())
    output_str = re.search(r"!.*end",output_str,flags=re.DOTALL).group(0)
    with open(f"{ip}.cfg".format(ip), mode="w") as f:
        f.write(output_str)
    print(f"Successfully backup device {ip} ")
ssh_client.close()
    
    



