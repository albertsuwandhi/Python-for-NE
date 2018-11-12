#!/usr/bin/env python3
ip_addr_list = ['1.1.1.1','2.2.2.2','8.8.8.8','8.8.4.4']
ip_addr_list2 = ['10.10.10.10','20.20.20.20']
print("ip_addr_list : ", ip_addr_list)
for ip in ip_addr_list:
    print("IP Address :", ip)
print("-"*80)
#var will be a two elements tuple
for var in enumerate(ip_addr_list,1):
    print(var)
print("-"*80)
for idx,ip in enumerate(ip_addr_list,1):
    print(f"{idx} element is {ip}")
print("-"*80)
for ip in ip_addr_list:
    print("IP Address :", ip)
    if ip == '8.8.8.8':
        break
print("-"*80)
for ip in ip_addr_list:
    if ip == '8.8.8.8':
        continue
    print("IP Address :", ip)
print("-"*80)
#nested loop
for ip in ip_addr_list:
    for ip2 in ip_addr_list2:
        print(ip)
        print(ip2)
print("-"*80)
#range
for i in range(len(ip_addr_list)):
    print(f"{i} : ", ip_addr_list[i])
print("-"*80)
print(f"8.8.8.8 is in ip_addr_list?", '8.8.8.8' in ip_addr_list)
print(f"10.8.8.8 is in ip_addr_list?", '10.8.8.8' in ip_addr_list)