#/usr/bin/env python
import xmltodict
from pprint import pprint
with open("interface.xml","r") as f:
    xml_example = f.read()
pprint(xml_example)
print("--------------------------------------------------------------------------------")
xml_dict = xmltodict.parse(xml_example)
pprint(xml_dict)
print("--------------------------------------------------------------------------------")
print(xml_dict["interface"]["name"])
xml_dict["interface"]["name"] = "GigabitEthernet10"
print("--------------------------------------------------------------------------------")
print(xmltodict.unparse(xml_dict))
print("--------------------------------------------------------------------------------")





