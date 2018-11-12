#/usr/bin/env python
from napalm import get_network_driver
import json
import re
from getpass import getpass
strip_config = True
ip_addresses = ["10.8.32.249","10.8.32.250","10.8.32.251","10.8.32.252","10.8.32.254"]
#ip_addresses = ["10.8.32.251","10.8.32.252"]
print("============================ BACKUP CONFIG ============================")
user = input("Username : " )
password = getpass("Password : ")
for ip in ip_addresses:
    print(f"Connecting to Switch {ip}!")
    driver = get_network_driver("ios")
    Router = driver(ip,user,password)
    # If SSH user different port, eq : 2222
    #Router = driver(f"192.168.160.135","admin","admin123,optional_args"={"port": 2222})
    Router.open()
    output = Router.get_config()
    running_config = output["running"]
    startup_config = output["startup"]
    if strip_config:
        running_config = re.search(r"!.*end",running_config,flags=re.DOTALL).group(0)
        startup_config = re.search(r"!.*end",startup_config,flags=re.DOTALL).group(0)
    with open(f"running_{ip}.cfg",mode="w") as f:
        f.write(running_config)
    with open(f"startup_{ip}.cfg",mode="w") as f:
        f.write(startup_config)
    print(f"Backup of running and startup configs for {ip} SUCCESS!")
    print("----------------------------------------------------------------------")
Router.close()


