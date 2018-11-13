import nmap
count = 0
ip_open = []
with open("ip.txt","r") as f:
    ip_list = f.read().splitlines()
    print (ip_list)
nmap = nmap.PortScanner() 
for ip in ip_list:
    resp = nmap.scan(ip, "80")
    if resp['scan'][ip]['tcp'][80]['state'] == "open":
       count += 1
       ip_open.append(ip)
print '{} hosts open on port {} from total {} hosts'.format(count,80,len(ip_list))
print 'The hosts with opened ports are : {}'. format(ip_open)