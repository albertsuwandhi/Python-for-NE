#!/usr/bin/env python3
import re
with open("D:\Python\Python for NE\show_ver.txt",mode="r") as f:
    output=f.read()
#print(output)
show_ver = output.splitlines()
#print(show_ver[0])
line = show_ver[0]
print(line)
print('re.search(r"^C.*$",line).group(0) : ',re.search(r"^C.*$",line).group(0))
#print('re.search(r"i.*$",line).group(0) : ',re.search(r"i.*$",line).group(0))
print('re.search(r"^C.*$",line) : ',re.search(r"^CISCO.*, Version (\S+),.*$",line))
print('re.search(r"^CISCO.*, Version (\S+),.*$",line).group(1) : ',re.search(r"^CISCO.*, Version (\S+),.*$",line).group(1))
print('re.search(r"^CISCO (.*), Version (\S+),.*$",line).group(1) : ',re.search(r"^CISCO (.*), Version (\S+),.*$",line).group(1))
print('re.search(r"^CISCO (.*), Version (\S+),.*$",line).group(2) : ',re.search(r"^CISCO (.*), Version (\S+),.*$",line).group(2))
print('re.search(r"^CISCO (.*), Version (\S+),.*$",line).group(2) : ',re.search(r"^CISCO (.*), Version (?P<IOS_VER>\S+),.*$",line).groupdict())