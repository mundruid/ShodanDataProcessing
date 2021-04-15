"""Use the Shodan API to lookup CVEs for specific public IP addresses."""
import pprint
import json
import shodan
import os


def get_host_services(ip, token):
    """Return all runing services for a host.

    Args:
        ip (str): host IP
        token (str): Shodan key

    Returns:
        [type]: [description]
    """
    api = shodan.Shodan(token)
    host_services = api.host(ip)
    return host_services


def print_cves(ports, token):
    """[summary]

    Args:
        ports ([type]): [description]
        token ([type]): [description]
    """
    api = shodan.Shodan(token)

    for port in ports:
        try:
            exploits = api.exploits.search(f'port: {port}')

            for exploit in exploits['matches']:
                print(f'CVE: {exploit["cve"]}')
                print('Description: {exploit["description"]}')
                print(exploit)
                print('')

        except Exception as e:
            print(e)


def main():
    """Main entrypoint"""
    env = os.environ.get
    token = env("SHODAN_TOKEN", "")

    resp = get_host_services('8.8.8.8', token)
    pprint.pprint(resp)
    print_cves(resp['ports'], token)


if __name__ == "__main__":
    main()
