#!/usr/bin/env python3

class IPAddress(object):
    def __init__(self, ip='10.10.10.10', subnet='255.255.255.0'):
        self.ip = ip
        self.subnet = subnet
    def print_ip(self):
        print("IP : {} Subnet : {}".format(self.ip, self.subnet))

ip1 = IPAddress()
ip1.print_ip()

ip2 = IPAddress('11.1.1.1','255.255.255.240')
ip2.print_ip()


