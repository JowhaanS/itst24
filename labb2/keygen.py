import argparse
from cryptography.fernet import Fernet

def generate_key(name):
    key = Fernet.generate_key()
    with open(f'{name}.key', 'wb') as key_file:
        key_file.write(key)
    print(f'The key is generated and saved as "{name}.key".')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a symmetric key')
    parser.add_argument('-n', '--name', help='Name of key file.', default='secret')
    args = parser.parse_args()
    generate_key(args.name)
