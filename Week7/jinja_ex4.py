#/usr/bin/env python
import csv
import jinja2
with open("bgp_vars.csv", mode="r") as f:
    read_csv = csv.DictReader(f)
    for bgp_vars in read_csv:
        print(bgp_vars)
        advertised_routes = bgp_vars["adv_routes"]
        advertised_routes = advertised_routes.split()
        bgp_vars["adv_routes"] = advertised_routes
        print(bgp_vars)
        with open("nxos_bgp_csv.j2", mode="r") as f:
            bgp_template = f.read()
        t = jinja2.Template(bgp_template)
        print()
        print("--------------------------------------------")
        print(t.render(bgp_vars))
        print("--------------------------------------------")




