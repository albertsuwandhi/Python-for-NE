#!/usr/bin/env python3

ip_addr = ['1.1.1.1','2.2.2.2','3.3.3.3','8.8.8.8','8.8.4.4','1.1.1.1']
print("ip_addr = ", ip_addr)
set_ips = set(ip_addr)
print("set_ips = ", set_ips)
print("type set_ips = ", type(set_ips))
print("-"*80)

set_1 = {'1.1.1.1','2.2.2.2','3.3.3.3','8.8.8.8','8.8.4.4'}
set_2 = {'10.10.10.10','20.20.20.20','30.30.30.30','1.1.1.1'}
print(set_1)
print(set_2)
print("set_1 | set_2 : ", set_1 | set_2) #set_1.union(set_2)
print("set_1 & set_2 : ", set_1 & set_2) #set_1.intersection(set_2)
print("set_1 - set_2 : ", set_1 - set_2)
print("set_1 ^ set_2 : ", set_1 ^ set_2) #set_1.symmetric_difference(set_2)
