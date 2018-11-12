#!/usr/bin/env python3

from print_ip import print_ip
from pprint import pprint
import sys
#import print_ip
#print_ip.print_ip('10.10.10.10', 'root', 'toor')
print_ip('10.10.10.10', 'root', 'toor')

#where to find module? (IMPORT)
pprint(sys.path)