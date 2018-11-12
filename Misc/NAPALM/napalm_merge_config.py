#/usr/bin/env python
from napalm import get_network_driver
import json
print(f"Connecting to Router 192.168.160.132!")
driver = get_network_driver("ios")
Router = driver(f"192.168.160.132","admin","admin123",optional_args={"dest_file_system": "flash"})
#Router = driver(f"192.168.160.132","admin","admin123",optional_args={"dest_file_system": "nvram"})
Router.open()
Router.load_merge_candidate(filename = "Router_conf.txt")
print(Router.compare_config())
Router.commit_config()
Router.close()


