import subprocess

def change(interface, new_mac):
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

	subprocess.call("ifconfig "+interface+" | grep ether", shell=True)

		