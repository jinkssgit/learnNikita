#!/usr/bin/env python

import subprocess
import optparse


def get_args():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
	parser.add_option("-m", "--mac", dest="newmac", help="New MAC Address")
	(options, arguments) = parser.parse_args()
	return options

def grep_mac(interface):
	subprocess.call("ifconfig "+interface+" | grep ether", shell=True)

def mac_change(interface, new_mac):
	print("[+] Changing MAC for " + interface + " to new -> " + new_mac)

	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

	grep_mac(interface)


mac_change(get_args().interface, get_args().newmac)



