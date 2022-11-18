#ssh routers from deveices file
#connect to multiple routers mentioned in devices.txt
 
from netmiko import ConnectHandler

with open('devices.txt') as routers:

    for IP in routers:
	    Router = {
		   "device_type": "cisco_ios",
		   "ip": "sandbox_iosxe-latest-1.cisco.com",
		   "username": "developer",
		   "password": "Cisco12345"
        }           
        
        net_connect = ConnectHandler(**Router)
        print('connecting to ' + IP)
        print('-'*79)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*79)
net_connect.disconnect()