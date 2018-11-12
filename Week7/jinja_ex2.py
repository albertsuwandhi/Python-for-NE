#/usr/bin/env python
import jinja2
bgp_vars ={
    "local_as" : "100",
    "remote_ip_1" : "1.1.1.1",
    "remote_as_1" : "200",
    "adv_route_1" : "172.16.0.0/16",
    "adv_route_2" : "10.88.0.0/16",    
}

with open("nxos_bgp.j2", mode="r") as f:
    bgp_template = f.read()

t = jinja2.Template(bgp_template)
print(t.render(bgp_vars))


