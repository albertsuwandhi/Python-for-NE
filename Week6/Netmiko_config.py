#!/usr/bin/env python3
from netmiko import Netmiko
from getpass import getpass
#admin, admin123
password = getpass(prompt="Password : ")
IOU1 = {
    'ip' : '192.168.160.131',
    'username' : 'admin',
    'password'  : password, 
    'secret' : password,
    'device_type' : 'cisco_ios',
}
IOU2 = {
    'ip' : '192.168.160.132',
    'username' : 'admin',
    'password'  : password, 
    'secret' : password,
    'device_type' : 'cisco_ios',
}

my_routers = [IOU1, IOU2]
net_conn = Netmiko(**IOU1)

print(net_conn.find_prompt())
# send_command for execute command not in config mode
print(net_conn.send_command("show run | inc hostname"))
set1 = ['hostname IOU_1', 'logging console']
#send config from list
print(net_conn.send_config_set(set1))
#send from file
print("send config from file")
print(net_conn.send_config_from_file("D:/Python/Python for NE/Week6/config.txt"))

for device_ip in my_routers:
    net_conn = Netmiko(**device_ip)
    print(f"----- Interface UP on router {device_ip} -----")
    print(net_conn.send_command("show ip int bri | inc up"))









