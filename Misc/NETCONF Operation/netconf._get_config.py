#/usr/bin/env python
from ncclient import manager
import xmltodict
from pprint import pprint

#Example CSR1000V
router = {
    "ip":"192.168.160.135",
    "user":"admin",
    "pass":"admin",
    "port":"830",
}

netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
</filter>
"""     
netconf_conn = manager.connect(host=router["ip"],
                               port=router["port"],
                               username=router["user"],
                               password=router["pass"],
                               hostkey_verify=False)
interface_netconf = netconf_conn.get_config("running", netconf_filter)
netconf_response = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
pprint(netconf_response)
pprint(netconf_response["interfaces"]["interface"]["name"]["#text"])

