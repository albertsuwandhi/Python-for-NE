#!/usr/bin/env python3
from netmiko import Netmiko
from getpass import getpass
#please install https://github.com/networktocode/ntc-templates
#and then set the NET_TEXTFSM environment variable to point to the ./ntc-templates/templates
#directory.

# Credential in GNS3 : admin, admin123
password = getpass(prompt="Password : ")
IOU1 = {
    'host' : '192.168.160.131',
    'username' : 'admin',
    'password'  : password, 
    'secret' : password,
    'device_type' : 'cisco_ios',
}
net_conn = Netmiko(**IOU1)
output = net_conn.send_command("show ip arp")
print(output)
print(type(output))
output = net_conn.send_command("show ip arp", use_textfsm=True)
print(output)
print(type(output))







