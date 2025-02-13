import logging
import nmap

def log_result(units):
    for unit in units:
        logging.info(f"IP: {unit['ip']} Hostname: {unit['hostname']}")
        for service in unit['service']:
            logging.info(f"Port: {service['port']} Service: {service['service']} Version: {service['version']}")

#Scan a network or a single IP using nmap, shows ip, hostname*, open ports, services and versions*
#Prints a readable result and it uses logging to log if you wish to log it.
#* If it can detect it.
def scan_network(network, do_log):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=network, arguments='-sV')  
    units = []
    for host in scanner.all_hosts():
        if scanner[host].state() == 'up':
            hostname = scanner[host].hostname() or 'N/A'
            unit = {'ip': host, 'hostname': hostname, 'service': []}
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                for port in ports:
                    service = {
                        'port': port,
                        'service': scanner[host][proto][port]['name'],
                        'version': scanner[host][proto][port]['version']
                    }
                    unit['service'].append(service)
            units.append(unit)

    if do_log:
        logging.basicConfig(filename='networklog.log', level=logging.INFO)
        log_result(units)
        print('Scan complete')
    else:
        for unit in units:
            print(f"IP: {unit['ip']}, Hostname: {unit['hostname']}")
            for service in unit['service']:
                    print(f"Port: {service['port']} Service: {service['service']} Version: {service['version']}")
