#!/usr/bin/env python3
ipv4 = '192.168.100.254'
print("ipv4      : ", ipv4)
ipv4_list = ipv4.split(".")

print("ipv4_list : ", ipv4_list)
print('--- Join List --- : ".".join(ipv4_list)')
ipv4_join = ".".join(ipv4_list)
(print("ipv4_join : ", ipv4_join))
print("-"*80)
macaddr = '2c:44:a1:f1:00:01'
print("macaddr        : ", macaddr)
macaddr_list = macaddr.split(":")
print("macaddr_list   : ", macaddr_list)
print('--- Join List --- : "-".join(macaddr_list)')
macaddr_join = "-".join(macaddr_list)
(print("macaddr_join  : ", macaddr_join))






