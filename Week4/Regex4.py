#!/usr/bin/env python3
import re
with open("d:/Python/Python For NE/Misc/show_ver.txt",mode="r") as f:
    output=f.read()
print(output)
#SUB METHOD
output_sub = re.sub(r"^CISCO","Cisco", output,flags=re.M)
print(output_sub)
output_sub = re.sub(r"^CISCO.*","Cisco", output,flags=re.M)
print(output_sub)
#SPLIT METHOD
output_sub = re.split(r"\n",output)
print(output_sub)

#See also Find All Method



