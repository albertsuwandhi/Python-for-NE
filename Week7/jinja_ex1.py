#/usr/bin/env python
import jinja2
bgp_vars ={
    "local_as" : "100",
    "remote_ip_1" : "1.1.1.1",
    "remote_as_1" : "200",
    "adv_route_1" : "172.16.0.0/16",
    "adv_route_2" : "10.88.0.0/16",    
}

bgp_template = '''
feature bgp
router bgp {{local_as}}
  addess-family ipv4 unicast
    network {{adv_route_1}}
    network {{adv_route_2}}
  neighbor {{remote_ip_1}} remote-as {{remote_as_1}}
    update source loopback1
    ebgp-multihop 2
    address-family ipv4 unicast
'''

t = jinja2.Template(bgp_template)
print(t.render(bgp_vars))


