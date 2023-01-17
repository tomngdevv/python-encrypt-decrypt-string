**Encryption and Decryption Script**

This script provides a simple way to encrypt and decrypt strings using the cryptography library and the argparse library to handle command-line arguments.

Requirements
- Python 3
- cryptography library
- OpenSSL library

You can install the cryptography library by running the following command in your terminal:

pip3 install cryptography
You will also need to have the OpenSSL library installed on your system. On MacOS, it should be pre-installed. If you are facing issues, you can try to install OpenSSL via brew:

brew install openssl

Usage

To encrypt a string:

python3 script.py --key <key> --encrypt <string>

To decrypt a string:

python3 script.py --key <key> --decrypt <ciphertext>
Replace <key> with your encryption key, <string> with the string you want to encrypt, and <ciphertext> with the ciphertext you want to decrypt.

You can also run the script without any arguments to see the help message and get an idea of the options available.

Note: The script uses the same random salt for both encryption and decryption, if you want the decryption to work, you need to use the same key and the same salt used for encryption.

Example
python3 script.py --key "mysecretkey" --encrypt "mysecretmessage"
This command will encrypt the plaintext "mysecretmessage" and will print the ciphertext.

python3 script.py --key "mysecretkey" --decrypt "gAAAAABeaDY7YGd0F9X9MZQJEZV7k-t_vNz1wW8B5o5PnYJl5fX9xrkP5C5j5J5mI6g=="
This command will decrypt the ciphertext "gAAAAABeaDY7YGd0F9X9MZQJEZV7k-t_vNz1wW8B5o5PnYJl5fX9xrkP5C5j5J5mI6g==" and will print the plaintext.

You can adjust the script to meet your needs and make sure to use a strong and unique key for encryption and decryption.

Warning
This script is for demonstration purposes only. It is not recommended to use it in production as it does not handle exceptions and does not have any form of error handling.
