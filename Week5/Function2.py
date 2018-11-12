#!/usr/bin/env python3

my_list = ['192.168.10.10','admin','admin123']
my_dict ={
    'ip':'172.16.1.1',
    'username':'admin',
    'password':'Juniper123',
}
def print_ip(ip, username = 'albert', password = 'admin'):
     print("My IP : {} Username : {} Password : {}".format(ip, username, password))
# * pass list values as elements not as list entirely
print_ip(*my_list)
# ** pass dictionary values as elements not as dicts entirely
print_ip(**my_dict)

def test_func(func_list):
    print(func_list)
    func_list.append('123')

list1 = ['whatever']
test_func(list1)
print(list1)

#global var vs local var
ip_addr = '10.10.10.10'
def print_myip(ip_addr2):
    print("My IP is : ",ip_addr2)
    print("My IP (Global) is : ",ip_addr)

print_myip('1.1.1.1')

ip_addr = '11.11.11.11'
def print_myip(ip_addr):
    print("My IP is : ",ip_addr)

print_myip('2.2.2.2')



