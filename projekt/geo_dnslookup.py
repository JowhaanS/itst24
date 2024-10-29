import socket
import re
import requests

IPINFO_API_URL = 'http://ipinfo.io/{}/json'

def is_ip_address(query):
    ipv4_pattern = re.compile(r"^\d{1,3}(\.\d{1,3}){3}$")
    ipv6_pattern = re.compile(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$")
    if ipv4_pattern.match(query):
        return 'ipv4'
    elif ipv6_pattern.match(query):
        return 'ipv6'
    return None

def dns_lookup(domain, log):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Domain: {domain} -> IP: {ip_address}")
        get_geo_info(ip_address, log)
    except socket.gaierror:
        print(f"Can't find IP for the domain: {domain}")

def reverse_dns_lookup(ip_address, log):
    try:
        host_name = socket.gethostbyaddr(ip_address)[0]
        print(f"IP: {ip_address} -> Domain: {host_name}")
        get_geo_info(ip_address, log)
    except socket.herror:
        print(f"Can't find domain for the IP: {ip_address}")

def save_output_to_file(output, filename='gdnsl_output.txt'):
    """Saves the output to a .txt file, creating it if it doesn't exist."""
    with open(filename, 'a') as file:  # Open in append mode
        file.writelines(output)

def get_geo_info(ip_address, log):
    """Collects geo-info from an IP-adress from ipinfo.io."""
    try:
        response = requests.get(IPINFO_API_URL.format(ip_address))
        data = response.json()

        if 'bogon' in data:
            print(f"{ip_address} is a private or invalid IP-adress.")
            return

        city = data.get('city', 'Unknown')
        region = data.get('region', 'Unknown')
        country = data.get('country', 'Unknown')
        org = data.get('org', 'Unknown organisation')
        loc = data.get('loc', 'Unknown plats')

        try:
            domain = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            domain = 'Unknown domain'

        print(f"Geo-info for {ip_address}:")
        print(f"  Domain: {domain}")
        print(f"  City: {city}")
        print(f"  Region: {region}")
        print(f"  Country: {country}")
        print(f"  Location (lat,long): {loc}")
        print(f"  Organisation: {org}")

        geo_info = (
            f"Geo-info for {ip_address}:\n"
            f"  Domain: {domain}\n"
            f"  City: {city}\n"
            f"  Region: {region}\n"
            f"  Country: {country}\n"
            f"  Location (lat,long): {loc}\n"
            f"  Organisation: {org}\n"
        )

        if log:
            save_output_to_file(geo_info)

    except requests.RequestException as e:
        print(f"Something went wrong trying to get the geo-information: {e}")

def geo_dns_lookup(query, log):

    query_type = is_ip_address(query)

    if query_type == 'ipv4' or query_type == 'ipv6':
        reverse_dns_lookup(query, log)
    else:
        dns_lookup(query, log)
