import argparse
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt(key, plaintext):
    # Derive a key from the user input key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=b'random_salt',
        iterations=100000,
        backend=default_backend()
    )
    derived_key = base64.urlsafe_b64encode(kdf.derive(key))
    cipher = Fernet(derived_key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

def decrypt(key, ciphertext):
    # Derive a key from the user input key
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=b'random_salt',
        iterations=100000,
        backend=default_backend()
    )
    derived_key = base64.urlsafe_b64encode(kdf.derive(key))
    cipher = Fernet(derived_key)
    plaintext = cipher.decrypt(ciphertext).decode()
    return plaintext

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="Encryption key", required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--encrypt", help="Encrypt a string")
    group.add_argument("--decrypt", help="Decrypt a string")
    args = parser.parse_args()

    key = args.key.encode()

    if args.encrypt:
        plaintext = args.encrypt
        ciphertext = encrypt(key, plaintext)
        print("Encrypted string: ",ciphertext)
    elif args.decrypt:
        ciphertext = args.decrypt.encode()
        plaintext = decrypt(key, ciphertext)
        print("Decrypted string: ", plaintext)

if __name__ == "__main__":
    main()
