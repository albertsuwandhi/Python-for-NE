from __future__ import print_function, unicode_literals

ip_addr1 = '192.168.1.1'
ip_addr2 = "10.1.1.1"
ip_addr3 = '8.8.4.4'

print("-" * 80)
print("{} {} {}".format(ip_addr1, ip_addr2, ip_addr3))
#print('\n')
print("-"*80)
print("{:>20} {:>20} {:>20}".format(ip_addr1, ip_addr2, ip_addr3))
#print('\n')
print("-"*80)
print("{:^20} {:^20} {:^20}".format(ip_addr1, ip_addr2, ip_addr3))
#print('\n')
print("-"*80)

ip_addr4 = '10.20.30.40'
octets = ip_addr4.split(".")

print("{:^10} {:^10} {:^10} {:^10}".format(octets[0],octets[1], octets[2], octets[3]))
#print('\n')
print("-"*80)
print("{:^10} {:^10} {:^10} {:^10}".format(*octets))
#print('\n')
print("-"*80)
print("{ip_2:^20} {ip_1:^20} {ip_3:^20}".format(ip_1=ip_addr1, ip_2=ip_addr2, ip_3=ip_addr3))