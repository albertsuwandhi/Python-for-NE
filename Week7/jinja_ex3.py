#/usr/bin/env python

#take not on - in the for loop on Jinja template
import jinja2
adv_routes = ["172.16.0.0/16","10.88.0.0/16","192.168.100.0/24"]
bgp_vars ={
    "local_as" : "100",
    "remote_ip_1" : "1.1.1.1",
    "remote_as_1" : "200",
    "peer1_ipv6"  : True,
    "adv_routes"  : adv_routes,  
}
with open("nxos_bgp_loop.j2", mode="r") as f:
    bgp_template = f.read()

t = jinja2.Template(bgp_template)
print(t.render(bgp_vars))


