import subprocess
import optparse

# Projiect For Changing MAC in Linux
# develop by Jinkss
# v0.001
# Beta Test / Production
# Telegram
# -vv (Not realized)

interface = input("Input iterface: ")
new_mac = input("New MAC: ")

print("[+] Changing MAC for "+interface+" -> "+new_mac+" | Started...")
print("[/] Start down the interface")

print("interface -> "+interface)
print("New MAC -> "+ new_mac)
#subprocess.call("ifconfig "+interface+" down",shell=True)

print("[/] Completed succes")
print("[/] Start changing the MAC")


print("interface -> "+interface)
print("New MAC -> "+ new_mac)
#subprocess.call("ifconfig "+interface+" hw ether "+new_mac,shell=True)

print("[/] Completed succes")
print("[/] Start upping the interface")


print("interface -> "+interface)
print("New MAC -> "+ new_mac)
#subprocess.call("ifconfig "+interface+" up",shell=True)

print("[/] Completed succes")
