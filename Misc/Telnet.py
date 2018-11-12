#!/usr/bin/env python3
from telnetlib import Telnet
from getpass import getpass
my_router=['192.168.160.133','192.168.160.133']
for router in my_router:
    #if every router have different username and password
    username = input(f"Please enter {router} username:")
    password = getpass(f"Please enter {router} password:")
    tn = Telnet(router)
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


