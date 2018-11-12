#!/usr/bin/env python3

import json
my_dict = {'name':'Albert', 'age':36}
print(my_dict)
print("type : ", type(my_dict))

net_device = {}
net_device = {'vendor':'Cisco'}
net_device['ip_addr'] = '192.168.100.100'
dev_os = 'OS'
net_device[dev_os]='IOS-XE'
print(net_device)
print(net_device['vendor'])
print(net_device['ip_addr'])
print(net_device['OS'])
#print(net_device['Mode'])
print("Beautify using json.dumps()")
print(json.dumps(net_device, indent=3))
net_device2 = net_device
print(net_device2 is net_device)
print('-'*80)

print(list(net_device.items()))
print(net_device.get('vendor'))
print(net_device.get('mode',"not found"))
print(type(net_device.items()))
net_device['ip_addr'] = '192.168.100.111'
print('-'*80)

net_device2 = net_device.copy()
print(net_device2 is net_device)
print(net_device2)
print(type(net_device2))
net_device.pop('vendor')
print(net_device)
print('-'*80)

#print the key
for v in net_device2:
    print(v)
print("-"*80)

#print the values
for i in net_device2.values():
    print(i)
print("-"*80)

#print both hey and values
for i,j in net_device2.items():
    print(i,j)
print("-"*80)






