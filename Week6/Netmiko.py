#!/usr/bin/env python3
from netmiko import Netmiko
from getpass import getpass
#uncomment to generate error and show valid device type
#net_conn = Netmiko(host='192.168.160.131',username='admin',password=getpass(), device_type='F5')
net_conn = Netmiko(host='192.168.160.131',username='admin',password=getpass(), device_type='cisco_ios')
print(net_conn.find_prompt())

