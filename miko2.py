from netmiko import ConnectHandler

# First create the device object using dictionary
CSR = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
	}
# next establish the SSH connection

net_connect = ConnectHandler(**CSR)

# discover the hostname from the prompt

hostname = net_connect.send_command('show run | i host')
hostname.split(" ")
#hostname, device=hostname.split(" ")

hostanme ,device,*rest = hostname.split(" ")
 
print("Backing up " + device)

filename = "c:/Pythoncode/devices.txt"
#save backup in the samefolder as script use below 

showrun = net_connect.send_command('show run')
showrun = net_connect.send_command('show vlan')
showrun = net_connect.send_command('show ver')
log_file = open(filename, "a")   #in append mode
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")

net_connect.disconnect()
