#/usr/bin/env python
import json
filename = input("Please specify the JSON file : ")
#json_output1.json
#json_output2.json

with open(filename) as f:
    output = json.load(f)
print(f"Type of output is :", type(output))
print(f"Content of {filename} : ")
print(output)


