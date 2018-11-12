#/usr/bin/env python
from napalm import get_network_driver
import json
driver = get_network_driver("ios")
R1 = driver("192.168.160.131","admin","admin123")
R1.open()
output = R1.get_facts()
print(json.dumps(output, indent = 3))
R1.close()


