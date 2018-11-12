#!/usr/bin/env python3
from telnetlib import Telnet
from getpass import getpass
print("--- TELNET ---")
devices = input("Please enter filename : ")
username = input("Please enter username:")
password = getpass("Please enter password:")
f=open(devices, mode="r")
my_devices = f.readlines().strip("\n")
for device in my_devices:
    #if every router have different username and password
    print(f"Configuring {device}")
    tn = Telnet(device)
    tn.read_until("Username: ")
    tn.write(username + "\n")
    if password:
        tn.read_until("Password :")
        tn.write(password + "\n")
    tn.write("conf t\n")
    tn.write("vlan 100\n")
    tn.write("name Management\n")
    tn.write("vlan 200\n")
    tn.write("name Sales\n")
    tn.write("end\n")
    tn.write("exit\n")
print(tn.read_all())


