from shodan import Shodan
import json

api = Shodan('myKey')

# Lookup an IP
#ipinfo = api.host('8.8.8.8')
#print(ipinfo)

# Search for websites that have been "hacked"
#for banner in api.search_cursor('http.title:"hacked by "'):
#    print(banner)

# Get the total number of industrial control systems services on the Internet
ics_services = api.count('tag:ics')
print('Industrial Control Systems: {}'.format(ics_services['total']))

# Get the total number of industrial control systems services on the Internet
routers = api.count('router')
print('Routers: {}'.format(routers['total']))

# Get webcam total number
webcams = api.count('webcam')
# print(webcams)
print('Webcams total: {}'.format(webcams['total']))
specific_webcam = api.host('67.198.13.57')
for item in specific_webcam:
    print(item, specific_webcam[item])