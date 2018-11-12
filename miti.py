# Author: Dr. X
# look for specific model exploits
# count how many exploits of a specific type

import shodan

SHODAN_API_KEY = "myKEy"

api = shodan.Shodan(SHODAN_API_KEY)

# Wrap the request in a try/ except block to catch errors
webcams = ['TP-Link', 'axis', 'D-Link', 'Dericam', 'Foscam', 'Icam', 'KaiKong', 'Loftek', 'Coolcam', 'Netcam', 'Panasonic', 'Polaroid', 'Pyle', 'Safehome', 'Sricam', 'Vstarcam', 'Wanscam']
routers = ['netgear', 'linksys', 'Asus', 'Tenda']
assistants = ['Amazon Echo', 'Google Home']
printers = ['Brother', 'HP OfficeJet', 'HP LaserJet', 'Canon', 'Epson']
# lights = ['', 'router', 'Amazon Echo', 'printer', 'light']
exploits_type = ['dos', 'local', 'remote', 'webapps']
exploits_platform = ['windows', 'php', 'linux', 'hardware']

# change list for every run
for device in printers:
    for type in exploits_type:
        # Search Shodan
        print('Searching for '+ device)
        print('=================================================================================')
        print('exploit search ' + type)
        print('=================================================================================')
        # Wrap the request in a try/ except block to catch errors
        try:
            # Search Shodan
            exploits = api.exploits.search(device + ' type:'+ type)
            #windows = api.exploits.search(device + ' type:'+ type + ' platform:windows')
            #linux = api.exploits.search(device + ' type:'+ type + ' platform:linux')
            #hardware = api.exploits.search(device + ' type:'+ type + ' platform:hardware')

            # Show the results
            print('Exploits found: {}'.format(exploits['total']))
            #print('Windows found: {}'.format(windows['total']))
            #print('Linux found: {}'.format(linux['total']))
            #print('Hardware found: {}'.format(hardware['total']))
            for exploit in exploits['matches']:
                print('CVE: {}'.format(exploit['cve']))
                print('Description: {}'.format(exploit['description']))
                print('Platform: {}'.format(exploit['platform']))
                #print(exploit)
                print('')
        except Exception as e:
            print(e)
