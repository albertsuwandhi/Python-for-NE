import socket
import time
import multiping
domain_list = ["www.cisco.cccccc","www.detik.com","www.google.co.id"]
for domain in domain_list:
    try:
        addr = socket.gethostbyname(domain)
    except:
        print(f"Can't resolved {domain}")
        continue
    print(addr)

