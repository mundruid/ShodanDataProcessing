# Author: Dr. X
# look for specific model exploits
# count how many exploits of a specific type

import shodan

SHODAN_API_KEY = "myKey"

api = shodan.Shodan(SHODAN_API_KEY)

# Wrap the request in a try/ except block to catch errors
devices = ['webcam',  'TP-Link', 'axis', 'D-Link', 'Dericam', 'Foscam', 'Icam', 'KaiKong', 'Loftek', 'Coolcam', 'Netcam', 'Panasonic', 'Polaroid', 'Pyle', 'Safehome', 'Sricam', 'Vstarcam', 'Wanscam', 'router', 'netgear', 'linksys', 'Asus', 'Tenda', 'Amazon Echo', 'Google Home', 'printer', 'Brother', 'HP OfficeJet', 'HP LaserJet', 'Canon', 'Epson']
# lights = ['', 'router', 'Amazon Echo', 'printer', 'light']
exploits_type = ['dos', 'local', 'remote', 'webapps']
exploits_platform = ['windows', 'php', 'linux', 'hardware']

print('Device, number of telnet, number of http, number of https, port 8081, port 8080, port 21, port 137, number of samba, number of netbios')
for device in devices:
    try:
        results = api.search(device)
        num_telnet = api.search(device + ' port:23')
        num_http = api.search(device + ' port:80')
        num_https = api.search(device + ' port:443')
        num_8081 = api.search(device + ' port:8081')
        num_8080 = api.search(device + ' port:8080')
        num_ftp = api.search(device + ' port:21')
        num_137 = api.search(device + ' port:137')
        num_samba = api.search(device+ ' product:samba')
        #num_netbios = api.search('webcam product:netbios')
        print(device + ', ' + str(results['total']) + ', ' + str(num_telnet['total']) + ', ' + str(num_http['total']) + ', ' + str(num_https['total']) + ', ' + str(num_8081['total']) + ', ' + str(num_8080['total']) + ', ' + str(num_21['total']) + ', ' + str(num_137['total']) + ', ' + str(num_samba['total']))
    except Exception as e:
        print(e)

# change word and list
#for device in webcams:
#    print('Searching for '+ device)
#    print('=================================================================================')
    # Wrap the request in a try/ except block to catch errors
#    try:
        # Search Shodan
        # change word and list
#        print('Webcam, number of telnet, number of http, number of https, port 8081, port 137, number of samba, number of netbios')
#        results = api.search(device + ' webcam')
#        telnet = api.search(device + ' webcam port:23')
        #http = api.search(device + ' webcam port:80')
        #http1 = api.search(device + ' webcam port:8080')
        #http2 = api.search(device + ' webcam port:8081')
        #samba = api.search(device + ' webcam product:samba')
        #netbios = api.search(device + ' webcam port:137')

        # Show the results
#        print('Results found: {}'.format(telnet['total']))
        #print('Port {}'.format(results['port']))
        #print(telnet['total'] + ', ' + http['total'] + ', ' + http1['total'] + ', ' + http2['total'] + ', ' + samba['total'] + ', ' + netbios['total'] )
#        print('')
#    except Exception as e:
#        print(e)
