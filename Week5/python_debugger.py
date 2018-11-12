#!/usr/bin/env python3

import pdb
def print_ip(ip, username = 'admin', password = 'pass123'):
    print("My IP : {} Username : {} Password : {}".format(ip, username, password))
    return
if __name__ == '__main__':
    #-- set BP Command --
    #pdb.set_trace() 
    print_ip('1.1.1.1')

# List Line : list x, y
# b line_number = set Break Points
# s = single step
# up/down = back one step
# args = see arguments
# !var_name = x --> Change Argument Value
# p var_name = see variable content/value
# run program with PDD : python -m pdb code.py

