# Author: Dr. X
# look for specific model exploits
# count how many exploits of a specific type

import shodan
import time
import csv

f = open("myKey.txt")
myKey = f.readline()
SHODAN_API_KEY = str(myKey)

api = shodan.Shodan(SHODAN_API_KEY)
f.close()

# read devices from file
input_file_devices = 'devices.csv'
devices_data = dict()
with open(input_file_devices, 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        devices_data[row[0]] = (row[1:])

print('Device, number of telnet, number of http, number of https, port 8081, port 8080, port 21, port 137, number of samba, number of netbios')
for dev_item in devices_data:
    #          # Search Shodan
    print('Searching for '+ dev_item)
    for model in devices_data[dev_item]:
        try:
                results = api.search(model)
                num_telnet = api.search(model + ' port:23')
                #     num_http = api.search(device + ' port:80')
                #     num_https = api.search(device + ' port:443')
                #     num_8081 = api.search(device + ' port:8081')
                #     num_8080 = api.search(device + ' port:8080')
                #     num_ftp = api.search(device + ' port:21')
                #     num_137 = api.search(device + ' port:137')
                #     num_samba = api.search(device+ ' product:samba')
                # #num_netbios = api.search('webcam product:netbios')
                # print(device + ', ' + str(results['total']) + ', ' + str(num_telnet['total']) + ', ' + str(num_http['total']) + ', ' + str(num_https['total']) + ', ' + str(num_8081['total']) + ', ' + str(num_8080['total']) + ', ' + str(num_ftp['total']) + ', ' + str(num_137['total']) + ', ' + str(num_samba['total']))
                print(model + ', ' + str(results['total']) + ', ' + str(num_telnet['total']))
                time.sleep(20)
        except Exception as e:
                print(e)