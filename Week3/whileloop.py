#!/usr/bin/env python3
ip_addr_list = ['1.1.1.1','2.2.2.2','8.8.8.8','8.8.4.4','10.10.10.10']
i = 0
while i<=2:
    print(ip_addr_list[i])
    i += 1
print("-"*80)

for ip in ip_addr_list:
    print(ip)
    if ip == '8.8.2.2':
        break
#the else statement won't be executed if loop exit by break
#else statement will be executed on normal exhaustion of loop
else: 
    print("Else")
