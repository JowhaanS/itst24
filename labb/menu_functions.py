import nmap
import os
from pathlib import Path
import re

ip_regex = r'\b((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\b'

def is_valid_ip(ip):
    if re.fullmatch(ip_regex, ip):
        return True
    return False

def check_result_files():
    current_directory = Path(__file__).parent
    result = [file for file in current_directory.rglob("*.txt") if file.name != 'input.txt']
    if result:
        return result
    else:
        print('No saved scan results found!')

def create_input_file(input_for_scan):
    with open(input_for_scan, 'w') as file:
           file.write 

def read_input_file(input_for_scan):
    if os.path.exists(input_for_scan):
        with open(input_for_scan, 'r') as file:
            lines = file.readlines()
            if lines:
                print()
                for line in lines:
                    print(line.strip())
            else: 
                print("The file doesn't contain anything")
    else:
        create_input_file(input_for_scan)
        print(f"First time running, created {input_for_scan}")
    
def append_input_file(input_for_scan, ip):
    if os.path.exists(input_for_scan):
        with open(input_for_scan, 'a') as file:
            file.write(ip + '\n')
        print(f"IP adress {ip} added to {input_for_scan} \n")
    else:
        create_input_file(input_for_scan)
        print(f"First time running, created {input_for_scan}")

def search_file(input_for_scan, ip):
    if os.path.exists(input_for_scan):
        with open(input_for_scan, 'r') as file:
            lines = file.readlines()
        matching_lines = [line for line in lines if ip in line]
        if not matching_lines:
            print("No IP address match")
        else:
            print(f"The IP {ip} was found")
            remove_from_input_file(input_for_scan, ip, lines)
    else:
        create_input_file(input_for_scan)
        print(f"First time running, created {input_for_scan}")

def remove_from_input_file(input_for_scan, ip, lines):
    if lines:
        confirmation = input(f"Are you sure you want to delete the line(s) containing {ip}? (y/n): ").lower()
        if confirmation == 'y':
            filtered_lines = [line for line in lines if ip not in line]
            with open(input_for_scan, 'w') as file:
                file.writelines(filtered_lines)
            print(f"The IP {ip} was removed.")
        else:
            print("Deletion canceled.")

# Saknar felhantering om det inte går att pinga host
def scan_from_input(ip):
    nm = nmap.PortScanner()
    nm.scan(ip)
    result = nm[ip]
    host_info = {
        'name': result['hostnames'][0]['name'] if result['hostnames'] else 'Unknown',
        'ipv4': result['addresses'].get('ipv4', 'Unknown'),
        'open_ports': []
    }
    
    for port, port_data in result['tcp'].items():
        if port_data['state'] == 'open':
            host_info['open_ports'].append({
                'port': port,
                'service': port_data['name']
            })
    
    return host_info

def extract_from_input(input_for_scan):
    if os.path.exists(input_for_scan):
        with open(input_for_scan, 'r') as file:
            lines = file.readlines()
            if lines:
                for line in lines:
                    if is_valid_ip(line.strip()):
                        print('Nmap scan in progres...')
                        print(line.strip())
                        result = scan_from_input(line.strip())
                        print_current_scan(result)
                        ask_to_save(result)
            else:
                print("No valid IP adress found")
    else:
        create_input_file(input_for_scan)
        print(
            f"First time running, created {input_for_scan}\n"
            "It's empty and needs to have at least 1 valid IP before scan")

def print_current_scan(result):
    print(f"Host Name: {result['name']}")
    print(f"IP Address: {result['ipv4']}")
    print("Open Ports:")
    for port in result['open_ports']:
        print(f" - Port {port['port']}: {port['service']}")

def ask_to_save(result):
    value = input("\nSCAN complete, do you wish to save the results y/n ?\n").lower()
    if value == 'y':
        save_result(result)

def save_result(result):
    filename = f"{result['ipv4']}.txt"
    with open(filename, 'w') as file:
        file.write(f"Host Name: {result['name']}\n")
        file.write(f"IP Address: {result['ipv4']}\n")
        file.write("Open Ports:\n")
        for port in result['open_ports']:
            file.write(f" - Port {port['port']}: {port['service']}\n")
    print(f'File saved to {filename}')

def show_result_files():
    result = check_result_files()
    for file in result: 
        print(file.name)

#Lägga till .txt på slutet så det räcker att man skriver IP ?
def read_result_file(filename):
    result = check_result_files()
    for file in result:
        if filename == file.name:
            with open(filename, 'r') as file:
                content = file.read()
                if content:
                    print(content.strip())
                    break
        else:
            print('No file with that name')