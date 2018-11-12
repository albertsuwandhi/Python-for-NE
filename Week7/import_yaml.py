#/usr/bin/env python
import yaml
from pprint import pprint
filename = input("Please specify the YAML file : ")
#yaml_ip1.yml : list
#yaml_ip2.yml : dictionary
#yaml_ip3.yml : list & dictionary, more complex data structure
#yaml_ip4.yml : list & dictionary, more complex data structure
with open(filename) as f:
    output = yaml.load(f)
print(f"Type of output is :", type(output))
print(f"Content of {filename} : ")
pprint(output)


