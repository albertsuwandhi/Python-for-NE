#!/usr/bin/env python3
def print_ip(ip, username = 'admin', password = 'pass123'):
    print("My IP : {} Username : {} Password : {}".format(ip, username, password))



if __name__ == '__main__':
    print_ip('1.1.1.1')