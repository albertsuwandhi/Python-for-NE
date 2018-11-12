#! /usr/bin/env python

from device_info import ios_xe1
from ncclient import manager

if __name__ == '__main__':
    with manager.connect(host=ios_xe1["address"], port=ios_xe1["port"],
                         username=ios_xe1["username"],
                         password=ios_xe1["password"],
                         hostkey_verify=False) as m:
        print("Here are the NETCONF Capabilities : ")
        for capability in m.server_capabilities:
            print(capability)
'''
Two General Capabilities 
 1. Base 
 2. Model

Data Model Details : 
 1. Model URI
 2. Module Name and Revision
 3. Protocol Features
 4. Deviations - Another Model that modifies this one 
'''