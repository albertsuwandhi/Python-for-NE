import sys
from ncclient import manager

def get_capabilities(host, port, user, pwd):
    with manager.connect(host=host, port=port, username=user, password=pwd, hostkey_verify=False, device_params={'name': 'csr'}) as m:
        capabilities =  m.server_capabilities

    return capabilities

def print_capabilities(c):
    file = open ("support.txt","w")
    for line in c:
        file.writelines(line+"\n")

host = str(sys.argv[1])
port = str(sys.argv[2])
username = str(sys.argv[3])
password = str(sys.argv[4])


x = get_capabilities (host,port,username,password)
a = print_capabilities(x)

## Using this Files
## ptyhon 1.get_capabilities.py {ip-address} {netconf-port} {username} {password}


