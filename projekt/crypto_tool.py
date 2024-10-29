import sys
import os
from cryptography.fernet import Fernet, InvalidToken

def confirm_overwrite(file_path):
    response = input(f'The file {file_path} will be overwritten. Are you sure? (y/n): ')
    if response.lower() != 'y':
        print('Operation cancelled.')
        sys.exit(0)
    return True

def load_key(key_file):
    if not os.path.exists(key_file):
        raise FileNotFoundError(f'Key file {key_file} not found.')
    with open(key_file, 'rb') as file:
        return file.read()

def encrypt_file(file_path, key):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File {file_path} not found.')
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    if confirm_overwrite(file_path):
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    print(f'File {file_path} has been encrypted.')

def decrypt_file(file_path, key):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File {file_path} not found.')
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except InvalidToken:
        print("Decryption failed: Invalid key or the file was not encrypted with Fernet.")
        return

    if confirm_overwrite(file_path):
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)

    print(f'File {file_path} has been decrypted.')
