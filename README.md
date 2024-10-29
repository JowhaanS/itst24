# Python Toolbox

### A collection of network and cryptographic tools built with Python 🛠️

This project is a Python-based "toolbox" created for a school project. It includes various utilities for encryption, decryption, DNS lookup, port scanning, packet sniffing, and more. The toolbox is powered by `argparse`, allowing the user to run specific tools from the command line. The toolbox aims to provide a basic set of tools for network and security tasks.

## Table of Contents
- [Features](#features)
  - [Crypto Tool](#crypto-tool)
  - [Geo-DNS Lookup](#dns-lookup)
  - [Nmap Scanner](#nmap-scanner)
  - [Packet Sniffer](#packet-sniffer)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### Crypto Tool
This tool allows you to **encrypt** and **decrypt** messages using the `Fernet` symmetric encryption algorithm from the `cryptography` library. Additionally, it can generate keys for use in the encryption process.

- **Encrypt:** Encrypts a given file using a generated or provided key.
- **Decrypt:** Decrypts an encrypted file using the correct key.
- **Key Generation:** Generates secure keys for encryption.

### DNS Lookup
Performs DNS lookups to resolve domain names and obtain additional information such as the server’s geographical location.

- **DNS Resolver:** Queries DNS servers using Python's `socket` module to retrieve IP addresses of domain names.
- **Geolocation:** Fetches the geographical information of the resolved IP using the [ipinfo.io](https://ipinfo.io) API.

### Nmap Scanner
A lightweight interface for performing basic port scanning using `nmap` functionality in Python.

- **Port Scan:** Scans a range of ports on a specified target.
- **Output Options:** Supports writing the scan results to an output file for later use.

### Packet Sniffer
A simple packet sniffer built using `Scapy` to capture and analyze network packets.

- **Packet Capture:** Sniffs network traffic on a specific interface.
- **Packet Analysis:** Displays or saves information on captured packets for further analysis.

---

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/JowhaanS/itst24.git
    ```

2. Navigate to the project directory:
    ```bash
    cd projekt
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

Run the `main.py` file with arguments to specify the tool and options you want to use. Here's a general overview:

```bash
python main.py <tool> [options]
```
## Examples
### Keygen
```bash
python main.py keygen
```
### Crypto tool
```bash
python main.py encrypt <input-file> <key>
python main.py decrypt <input-file> <key>
```
### Geo-DNS Lookup
```bash
python main.py gdnsl <domain-name or ip> [--log]
```
### Nmap Scanner
```bash
python main.py nmap <ip> [--log]
```
### Packet Sniffer
```bash
python main.py sniff -c <packet-count> -i <interface> -f <filter> [--output] [--verbose]
```

## Dependencies

Make sure you have Python 3.x installed. This project requires the following libraries, which can be installed via requirements.txt:

- cryptography (for encryption tools)
- socket (for DNS resolution)
- re (for regex handling in DNS lookups)
- requests (for IP geolocation using ipinfo.io)
- nmap (for network scanning)
- scapy (for packet sniffing)

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to create an issue or submit a pull request. Please ensure that any code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.