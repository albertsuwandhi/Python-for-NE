#!/usr/bin/env python3
from netmiko import Netmiko
from getpass import getpass
import re


#admin, admin123
password = getpass(prompt="Password : ")
IOU1 = {
    'host' : '192.168.160.131',
    'username' : 'admin',
    'password'  : password, 
    'secret' : password,
    'device_type' : 'cisco_ios',
}
IOU2 = {
    'host' : '192.168.160.132',
    'username' : 'admin',
    'password'  : password, 
    'secret' : password,
    'device_type' : 'cisco_ios',
}

my_routers = [IOU1, IOU2]
net_conn = Netmiko(**IOU1)
#disable --> >
net_conn.send_command_timing("disable")
print(net_conn.find_prompt())
#enable --> #
net_conn.enable()
print(net_conn.find_prompt())
#send_command wait for end of exec and don't show any command

output = net_conn.send_command("show ip int brief")
print(output)

output = net_conn.send_command("show ip int brief",expect_string=r"#")
print(output)






