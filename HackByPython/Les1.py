#!/usr/bin/env python

import optparse
import MAC

def get_args():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
	parser.add_option("-m", "--mac", dest="newmac", help="New MAC Address")
	(options, arguments) = parser.parse_args()
	return options


MAC.change(get_args().interface, get_args().newmac)