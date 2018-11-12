#!/usr/bin/env python3
import re
ip_addr = '10.220.110.1'
print("ip_addr : ", ip_addr)
# . any single character
print('re.search(r".", ip_addr).group(0) : ', re.search(r".", ip_addr).group(0))
print('re.search(r"....", ip_addr).group(0) : ', re.search(r"....", ip_addr).group(0))
# + one or more time
print('re.search(r".+", ip_addr).group(0) : ', re.search(r".+", ip_addr).group(0))
# * zero or more time, match null string also
print('re.search(r".*", ip_addr).group(0) : ', re.search(r".*", ip_addr).group(0))
print('re.search(r".*","": ', re.search(r".*", ""))
# ^ starts $ end
print('re.search(r"^.+$", ip_addr).group(0) : ', re.search(r"^.+$", ip_addr).group(0))
# \d digit
print('re.search(r"\d\d", ip_addr).group(0) : ', re.search(r"\d\d", ip_addr).group(0))
print('re.search(r"\d\d\d", ip_addr).group(0) : ', re.search(r"\d\d\d", ip_addr).group(0))
print('re.search(r"^\d\d\d", ip_addr) : ', re.search(r"^\d\d\d", ip_addr))
print('re.search(r"\d$", ip_addr) : ', re.search(r"\d$", ip_addr).group())
# \s white space
ip_addr ='   10.223.222.8   '
print('re.search(r"^\s+", ip_addr) : ', re.search(r"^\s+", ip_addr))
print('re.search(r"^\s+\d+", ip_addr) : ', re.search(r"^\s+\d+", ip_addr))
# \S NON white space
print('re.search(r"^\s+\S+", ip_addr) : ', re.search(r"^\s+\S+", ip_addr))
# Character Class
print('re.search("^\s+[\d\.]",ip_addr)', re.search("^\s+[\d\.]",ip_addr))
print('re.search("^\s+[\d\.]+",ip_addr)', re.search("^\s+[\d\.]+",ip_addr))
# () Parenthesis to save things
print('re.search(r"^\s+(\S+)", ip_addr) : ', re.search(r"^\s+(\S)+", ip_addr))
print('re.search(r"^\s+(\S+)", ip_addr).group(0) : ', re.search(r"^\s+(\S+)", ip_addr).group(0))
print('re.search(r"^\s+(\S+)", ip_addr).group(1) : ', re.search(r"^\s+(\S+)", ip_addr).group(1))


