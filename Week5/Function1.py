#!/usr/bin/env python3

def cetak(str1, str2):
    print(str1)
    print(str2)

cetak("hello", "world")

# By default will return None
def print_IP():
    print("My IP is 192.168.10.10")

#Take Arguments
def print_ip(*args):
    print("My IP : {} Username : {} Password : {}".format(*args))

# Function with defalt parameter
def print_ip2(ip, username = 'albert', password = 'admin'):
     print("My IP : {} Username : {} Password : {}".format(ip, username, password))

ret_val = print_IP()
print("Type of return value : ", type(ret_val))
print_ip('192.168.1.1','it','password')
print_ip2('8.8.8.8')
print_ip2('8.8.8.8',password='rahasia')
