#/usr/bin/env python
import yaml
from pprint import pprint
my_device_dict = {
 'rtr_1': {'bgp_peers': ['1.1.1.1', '2.2.2.2'],
           'device_type': 'cisco_ios',
           'ip': '10.10.10.10',
           'password': 'admin',
           'username': 'admin'},
 'rtr_2': {'bgp_peers': ['1.1.1.1', '3.3.3.3'],
           'device_type': 'juniper_junos',
           'ip': '10.10.10.20',
           'password': 'admin',
           'username': 'admin'},
 'rtr_3': {'bgp_peers': ['1.1.1.1', '3.3.3.3'], 'ip': '3.3.3.3'}
}
print("------- MY DEVICES DICTIONATY----------")
pprint(my_device_dict)
#use keys() to peeling the complex structured usually returned by API
print(my_device_dict.keys())
#normal formatting
with open("output_yaml1.yml", mode="w") as f:
    output = yaml.dump(my_device_dict,f, default_flow_style = False)

#compressed formatting
with open("output_yaml2.yml", mode="w") as f:
    output = yaml.dump(my_device_dict,f)


