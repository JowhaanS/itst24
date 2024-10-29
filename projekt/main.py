import argparse
import subprocess
import crypto_tool
import sniffer
import nmap_and_log
import geo_dnslookup

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
    'My little toolbox, includes symmetric keygen, '
    'encryption, decryption, basic nmap scan with logging option' 
    '& sniff network traffic using scapy')
    parser.add_argument('operation', choices=
    ['keygen', 'nmap', 'encrypt', 'decrypt', 'sniff', 'gdnsl'],
    help='Specify whether to generate a key, encrypt or decrypt a file or use nmap.')

    args, remaining_args = parser.parse_known_args()

match args.operation:
    case 'keygen':
        #Operation: keygen, generates a key, hardcoded name
        #Example: python main.py keygen
        subprocess.run(['python', 'keygen.py'], check=True)
    case 'nmap':
        #Operation nmap, basic scan used on my local range for testing, add flag to include a log not just prints.
        #Example python main.py nmap -l
        nmap_parser = argparse.ArgumentParser(description='Use nmap to scan an IP')
        nmap_parser.add_argument('ip', help='The IP to scan')
        nmap_parser.add_argument('-l', '--log', action='store_true',
        help='Chose wether or not to log results')
        nmap_args = nmap_parser.parse_args(remaining_args)
        nmap_and_log.scan_network(nmap_args.ip, nmap_args.log)
    case 'encrypt':
        #Operation: Encrypt a passed file and key
        #Example: python main.py encrypt secret.txt secret.key
        encrypt_parser = argparse.ArgumentParser(description='Encrypt a file')
        encrypt_parser.add_argument('input_file', help='The file to encrypt')
        encrypt_parser.add_argument('key_file', help='Path to the key file')
        encrypt_args = encrypt_parser.parse_args(remaining_args)
        key = crypto_tool.load_key(encrypt_args.key_file)
        crypto_tool.encrypt_file(encrypt_args.input_file, key)
    case 'decrypt':
        #Operation: Decrypt a passed file with correct key
        #Example: python main.py decrypt secret.txt secret.key
        decrypt_parser = argparse.ArgumentParser(description='Decrypt a file')
        decrypt_parser.add_argument('input_file', help='The file to decrypt')
        decrypt_parser.add_argument('key_file', help='Path to the key file')
        decrypt_args = decrypt_parser.parse_args(remaining_args)
        key = crypto_tool.load_key(decrypt_args.key_file)
        crypto_tool.decrypt_file(decrypt_args.input_file, key)
    case 'gdnsl':
        #Operation: DNS lookup with geo information
        #Example: python main.py gdnsl google.se -l
        gdnsl_parser = argparse.ArgumentParser(description='Enter a domain name or ip for dnslookup')
        gdnsl_parser.add_argument('query', help='Enter domain or IP')
        gdnsl_parser.add_argument('-l', '--log', action='store_true',
        help='Choose wether or not to log results')
        gdnsl_args = gdnsl_parser.parse_args(remaining_args)
        geo_dnslookup.geo_dns_lookup(gdnsl_args.query, gdnsl_args.log)
    case 'sniff':
        #Operation: Sniff network packages using Scapy, including interface/filter
        #You may save the output to view in wireshark if you wish
        #Example: python main.py sniff -c 10 -f tcp -o output
        sniff_parser = argparse.ArgumentParser('Sniff using scapy')
        sniff_parser.add_argument(
        "-i", "--interface", 
        type=str,
        default="en0",  # Default network interface (change as needed)
        help="Network interface to sniff on (e.g., eth0, wlan0)"
        )
        sniff_parser.add_argument(
        "-c", "--count", 
        type=int,
        default=0,  # 0 means capture indefinitely
        help="Number of packets to capture (default: 0 for infinite)"
        )
        sniff_parser.add_argument(
        "-f", "--filter", 
        type=str,
        default="",  # No filter by default
        help="BPF filter for packet sniffing (e.g., 'tcp', 'udp port 53')"
        )
        sniff_parser.add_argument(
        "-o", "--output", 
        type=str,
        help="Output file to save packets (PCAP format)"
        )
        sniff_parser.add_argument(
        "-v", "--verbose", 
        action="store_true",
        help="Increase output verbosity (show packet details)"
        )
        sniff_args = sniff_parser.parse_args(remaining_args)
        sniffer.sniff_packets(
        interface=sniff_args.interface,
        count=sniff_args.count,
        bpf_filter=sniff_args.filter,
        output_file=sniff_args.output,
        verbose=sniff_args.verbose)
