#/usr/bin/env python
import requests
import json
from pprint import pprint

router = {
    "ip":"192.168.160.135",
    "username":"admin",
    "password":"admin",
    "port":"443",
}

req_headers = {"Accept":"application/yang-data+json"}
url= "https://{}:{}/restconf/data/interfaces/interface=GigabitEthernet1".format(router["ip"],router["port"])

print("Request to URL : ", url)
response = requests.get(url,headers=req_headers,verify=False,auth=(router["username"],router["password"]))
#print(type(response))
response_txt = response.text
print("Response : \n", response_txt)
print("-------------------------------------------------------------------------------------------------")
api_data = response.json()
print(api_data["ietf-interfaces:interface"]["name"])
print("-------------------------------------------------------------------------------------------------")

url= "https://{}:{}/restconf/data/Cisco-IOS-XE-native:native/interface?fields=GigabitEthernet/ip/address/primary;name".format(router["ip"],router["port"])
print("Request to URL : ", url)
response = requests.get(url,headers=req_headers,verify=False,auth=(router["username"],router["password"]))
response_txt = response.text
print("Response : \n", response_txt)
print("-------------------------------------------------------------------------------------------------")








