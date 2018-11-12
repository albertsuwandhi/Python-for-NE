#!/usr/bin/env python3
import paramiko
import time
from getpass import getpass
print("--- Backup Switch Config  ---")
my_devices = ['10.8.32.250', '10.8.32.252']
username = input("Please enter username  : ")
password = getpass("Please enter password: ")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
for ip in my_devices:
    a = ssh_client.connect(ip,username=username,password=password)
    print(f"a is {a}")
    print(f"Successfully connect to {ip}")
    ssh_conn = ssh_client.invoke_shell()
    ssh_conn.recv(1000)
    ssh_conn.send("terminal length 0\n")
    time.sleep(1)
    ssh_conn.recv(1000)
    ssh_conn.send("show run")
    time.sleep(0.5)
    ssh_conn.recv(1000)
    ssh_conn.send("\n")
    time.sleep(0.5)
    ssh_conn.recv(0)
    time.sleep(2)
    if ssh_conn.recv_ready():
        output = ssh_conn.recv(65535)
    print(output.decode())
    #f = open(f"{ip}.cfg",mode = "w")
    #with open("{ip}.cfg".format(ip), mode="w") as f:
        #f.write(output)
    #print(f"Successfully backup device {ip}")
ssh_client.close()
    
    



