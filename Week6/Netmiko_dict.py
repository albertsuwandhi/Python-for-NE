#!/usr/bin/env python3
from netmiko import Netmiko
from getpass import getpass
#admin, admin123
IOU1 = {
    'host' : '192.168.160.131',
    'username' : 'admin',
    'password'  : getpass(), 
    'device_type' : 'cisco_ios',
}
IOU2 = {
    'host' : '192.168.160.132',
    'username' : 'admin',
    'password'  : getpass(), 
    'device_type' : 'cisco_ios',
}
#List of Dict
my_routers = [IOU1, IOU2]
for router in my_routers:
#** Pass Dict as argument list
    net_conn = Netmiko(**router)
    print(net_conn.find_prompt())


