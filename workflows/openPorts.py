# Author: Dr. X
# look for specific model exploits
# count how many exploits of a specific type

import shodan
import time
import datetime
import csv

f = open("myKey.txt")
myKey = f.readline()
SHODAN_API_KEY = str(myKey)

api = shodan.Shodan(SHODAN_API_KEY)
f.close()

# read devices from file
input_file_devices = './hosts/devices_small.csv'
input_file_ports = './attributes/ports_small.csv'
devices_data = dict()
with open(input_file_devices, 'r') as csv_file_devs:
    reader = csv.reader(csv_file_devs)
    for row in reader:
        devices_data[row[0]] = (row[1:])

ports_data = dict()
with open(input_file_ports, 'r') as csv_file_ports:
    reader = csv.reader(csv_file_ports)
    for row in reader:
        ports_data[row[0]] = (row[1:])

output_file_name = './data/ports' + str(datetime.datetime.now()) + '.csv'
output_file = open(output_file_name, 'w')

# print header row in output file
output_file.write('Device Type, Device Model')
for port_item in ports_data:
        output_file.write(', ' + port_item)
output_file.write('\n')

# print port results in output file
for dev_item in devices_data:
        for model in devices_data[dev_item]:
                # print device type, model, and how many devices were found
                try:
                        results = api.search(model)
                        output_file.write(dev_item + ', ' + model + ', ' + str(results['total']))
                except Exception as e:
                        print(e)
                # print ports per device model
                for port_item in ports_data:
                        for port in ports_data[port_item]:
                                try:
                                        num_ports = api.search(model + ' port ' + port)
                                        output_file.write(', ' + str(num_ports['total']))
                                        time.sleep(20)
                                except Exception as e:
                                        print(e)
                # done with csv line
                output_file.write('\n')

output_file.close()
csv_file_devs.close()
csv_file_ports.close()