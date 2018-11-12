#!/usr/bin/env python3
from netmiko import Netmiko
from getpass import getpass
#admin, admin123
password = getpass(prompt="Password : ")
IOU1 = {
    'host' : '192.168.160.131',
    'username' : 'admin',
    'password'  : password, 
    'secret' : password,
    'device_type' : 'cisco_ios',
}
net_conn = Netmiko(**IOU1)
filename = 'small_file.bin'
cmd = "delete flash:{}".format(filename)
#send command timing -- Wait
output = net_conn.send_command_timing(cmd)
if 'confirm' in output:
    output+=net_conn.send_command_timing("\n")
print(output)
net_conn.disconnect()

#allocate more time
output = net_conn.send_command_timing("copy run start",delay_factor=2)
#or can use
'''
IOU1 = {
    'host' : '192.168.160.131',
    'username' : 'admin',
    'password'  : password, 
    'secret' : password,
    'device_type' : 'cisco_ios',
    'global_delay_factor' : 2
}

'''

