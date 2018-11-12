#!/usr/bin/env python3

#1st Way 
from math import sqrt
#2nd Way
import re
my_str = 'MyIPAddress'
# use re.search instead of search
re.search(r"^M.+",my_str)
print("Location of re module : ", re.__file__)
#use sqrt only instead of math.sqrt
print("SQRT of 100 is : ", sqrt(100))


