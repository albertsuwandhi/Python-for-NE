#!/usr/bin/env python3
from __future__ import print_function
ip_addr1 = '192.168.1.123'
print ("Split ip_addr1 {}".format(ip_addr1))
result = ip_addr1.split(".")
print (result)
print (ip_addr1.split("192."))
#split return list

