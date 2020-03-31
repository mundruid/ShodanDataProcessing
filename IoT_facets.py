#!/usr/bin/env python
#
# query-summary.py
# Search Shodan and print summary information for the query.
#
# Author: achillean
# Modified by Dr. X to perform queries for different devices and add top ten ports, osses, devices, and CPEs

import shodan
import sys

# Configuration
f = open("myKey.txt")
myKey = f.readline()
SHODAN_API_KEY = str(myKey)

api = shodan.Shodan(SHODAN_API_KEY)
f.close()

# The list of properties we want summary information on
FACETS = [
    'org',
    'domain',
    ('port', 10),
    'asn',
    ('os', 10),
    'cpe',
    'device',

    # We only care about the top 3 countries, this is how we let Shodan know to return 3 instead of the
    # default 5 for a facet. If you want to see more than 5, you could do ('country', 1000) for example
    # to see the top 1,000 countries for a search query.
    ('country', 3),
]

FACET_TITLES = {
    'org': 'Top 5 Organizations',
    'domain': 'Top 5 Domains',
    'port': 'Top 10 Ports',
    'asn': 'Top 5 Autonomous Systems',
    'os': 'Top 10 Operating Systems',
    'cpe': 'Top 5 Common Platform Enumeration',
    'device': 'Top 5 Devices',
    'country': 'Top 3 Countries',
}

devices = ['TP-Link', 'axis', 'D-Link', 'Dericam', 'Panasonic', 'netgear', 'linksys', 'Asus', 'Tenda', 'Amazon Echo', 'Brother', 'HP OfficeJet', 'HP LaserJet', 'Canon', 'Epson']

# Input validation
#if len(sys.argv) == 1:
#    print('Usage: %s <search query>' % sys.argv[0])
#    sys.exit(1)

try:
    # Setup the api
    api = shodan.Shodan(API_KEY)

    # Generate a query string out of the command-line arguments
    #query = ' '.join(sys.argv[1:])
    for device in devices:
        query = device

        # Use the count() method because it doesn't return results and doesn't require a paid API plan
        # And it also runs faster than doing a search().
        result = api.count(query, facets=FACETS)

        print('Shodan Summary Information')
        print('Query: %s' % query)
        print('Total Results: %s\n' % result['total'])

        # Print the summary info from the facets
        for facet in result['facets']:
            print(FACET_TITLES[facet])

            for term in result['facets'][facet]:
                print('%s: %s' % (term['value'], term['count']))

            # Print an empty line between summary info
            print('')

except Exception as e:
    print('Error: %s' % e)
    sys.exit(1)
