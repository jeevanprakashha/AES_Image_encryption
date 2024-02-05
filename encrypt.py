from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from base64 import urlsafe_b64encode, urlsafe_b64decode
import secrets

def pad(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    return padded_data

def unpad(padded_data):
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

def encrypt_image(input_image_path, output_image_path, key, email):
    with open(input_image_path, 'rb') as f:
        plaintext = f.read()

    plaintext = pad(plaintext)
    iv = secrets.token_bytes(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(output_image_path, 'wb') as f:
        f.write(len(email).to_bytes(2, byteorder='big'))
        f.write(email.encode('utf-8'))
        f.write(iv + ciphertext)

if __name__ == "__main__":
    # Generate a random 32-byte (256-bit) key
    random_key = secrets.token_bytes(32)

    # Convert the random key to hexadecimal format for easier use
    hex_key = random_key.hex()

    print("Randomly generated key:", hex_key)

    # Replace 'your_key_here' with a 32-byte (256-bit) key in hexadecimal format
    key = bytes.fromhex(hex_key)

    # Get email ID from user input
    email = input("Enter the email ID to encrypt: ")

    input_image_path = '/Users/jeevanprakash/Documents/cyber_project/cyber_data/cd1.jpeg'
    output_image_path = '/Users/jeevanprakash/Documents/cyber_project/encrypt/enc50.enc'

    encrypt_image(input_image_path, output_image_path, key, email)
    print("Encryption complete.")
