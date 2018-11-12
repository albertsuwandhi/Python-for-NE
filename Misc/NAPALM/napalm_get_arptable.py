#/usr/bin/env python
from napalm import get_network_driver
import json
#192.168.160.131, 192.168.160.132
for i in range(1,3):
    print(f"Getting ARP Table on Router 192.168.160.13{i}!")
    driver = get_network_driver("ios")
    Router = driver(f"192.168.160.13{i}","admin","admin123")
    Router.open()
    output = Router.get_arp_table()
    print(json.dumps(output, indent = 3))
    print("----------------------------------------------------------")
Router.close()


