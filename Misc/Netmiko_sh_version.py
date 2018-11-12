#!/usr/bin/env python3
from netmiko import ConnectHandler
from getpass import getpass

ip_input = input("Masukkan file IP: ")
username = input("Masukkan username: ")
password = getpass()


file_ip = open(ip_input, "r")
list_ip = file_ip.readlines()

for ip in list_ip:
	device = {
		"device_type" : "cisco_ios",
		"ip" : ip,
		"username" : username,
		"password" : password,
	}

	print("Login to {}".format(ip))
	conn = ConnectHandler(**device)

	versi = conn.send_command("sh version")

	versi_file = open("v{0}.txt".format(ip.rstrip("\n")), "w")
	versi_file.write(versi)
	versi_file.close()
	#print "Versi {0} tersimpan!!".format(ip.rstrip("\n"))