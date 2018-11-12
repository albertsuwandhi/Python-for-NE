#!/usr/bin/env python3
import re
with open("d:/Python/Python for NE/Misc/show_ver.txt",mode="r") as f:
    output=f.read()
print(output)
show_ver = output.splitlines()
#print(show_ver[0])
line = show_ver[0]
print(line)
print('re.search(r"^CISCO (.*)",line).group(1) : ',re.search(r"^CISCO (.*)",line).group(1))
print('re.search(r"^CISCO (.*), ",line).group(1) : ',re.search(r"^CISCO (.*), ",line).group(1))
#use ? to limit the "greedy"
print('re.search(r"^CISCO (.*?), ",line).group(1) : ',re.search(r"^CISCO (.*?), ",line).group(1))
print('re.search(r"^CISCO (.*?)",line).group(0)) : ',re.search(r"^CISCO (.*?)",line).group(0))
print('re.search(r"^CISCO (.*?)",line).group(1) : ',re.search(r"^CISCO (.*?)",line).group(1))
# modify anchor ^ $ to each line instead of full --> use flags = re.M
print('Configuration Register is : ',re.search(r"^Configuration register is (.*)$",output))
print('Configuration Register is : ',re.search(r"^Configuration register is (.*)$",output, flags=re.M))
print('Configuration Register is : ',re.search(r"^Configuration register is (.*)$",output, flags=re.M).group(1))
# .* can not match new line, override with flags - re.DOTALL
print('re.search(r"^CISCO (.*)$",output) : ',re.search(r"^CISCO (.*)",output).group(0))
print('re.search(r"^CISCO (.*)$",output) : ',re.search(r"^CISCO (.*)",output, flags=re.DOTALL).group(0))
#print('Configuration Register is : ',re.search(r"^CISCO (.*)$",output, flags=re.M).group(1))

