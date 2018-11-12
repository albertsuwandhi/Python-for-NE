#/usr/bin/env python
import json
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

'''
my_random_dict = {'IPv6': True,
 'bgp': [{'neighbor': '10.1.1.1', 'remote-as': 1},
         {'neighbor': '10.1.2.2', 'remote-as': 2},
         {'neighbor': '10.1.3.3', 'remote-as': 3}],
 'id': 1,
 'ip_list': ['1.1.1.1', '2.2.2.2', '3.3.3.3'],
 'name': 'R1',
 'vlans': {11: 'IT', 22: 'HR', 33: 'Sales'}}

print(json.dumps(my_random_dict,indent=4))
'''
print(my_device_dict)
print(json.dumps(my_device_dict,indent=4))

with open("json_output2.json", mode="w") as f:
    json.dump(my_device_dict,f, indent=4)
print("Check json_output2.json")





