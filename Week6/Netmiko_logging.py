#!/usr/bin/env python3
from netmiko import Netmiko
from getpass import getpass
import logging
import time
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")


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
net_conn.write_channel("show ip arp\n")
time.sleep(15)
outout=net_conn.read_channel("show ip arp\n")
print(output)
print(type(output))









