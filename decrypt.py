from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from email.mime.text import MIMEText
import smtplib
import random

# Function to unpad the data
def unpad(data):
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(data) + unpadder.finalize()

def extract_email_from_encrypted_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as f:
        # Read the length of the email
        email_length = int.from_bytes(f.read(2), byteorder='big')

        # Read the email
        email = f.read(email_length).decode('utf-8')

    return email

def generate_otp():
    return random.randint(100000, 999999)

def send_otp_via_email(recipient_email, otp):
    sender_email = "encryptionimage3@gmail.com"
    sender_password = "nqcglhtmproxrdxm"

    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Create the email message
    message = MIMEText(f"Your OTP is: {otp}")
    message['Subject'] = 'Your OTP for Email Verification'
    message['From'] = sender_email
    message['To'] = recipient_email

    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())
    server.quit()

def get_user_otp_input():
    return input("Enter the OTP sent to your email: ")

def verify_otp(input_otp, sent_otp):
    return input_otp == sent_otp

def decrypt_image(input_image_path, output_image_path, key):
    with open(input_image_path, 'rb') as f:
        # Read the length of the email
        email_length = int.from_bytes(f.read(2), byteorder='big')

        # Read the email
        email = f.read(email_length).decode('utf-8')

        # Read the IV and ciphertext
        iv_ciphertext = f.read()

    # Extract the IV (Initialization Vector) from the data
    iv = iv_ciphertext[:16]
    ciphertext = iv_ciphertext[16:]

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

    # Create a decryptor object
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the decrypted data
    decrypted_data = unpad(decrypted_data)

    # Write the decrypted data to the output file
    otp = generate_otp()
    send_otp_via_email(email, otp)
    user_otp = get_user_otp_input()
    is_verified = verify_otp(user_otp, str(otp))
    if is_verified:
        with open(output_image_path, 'wb') as f:
            f.write(decrypted_data)
            print("Decryption complete. Data integrity verified.")
    else:
        print("Invalid OTP")

if __name__ == "__main__":
    # Take the key as input from the user
    key_input = input("Enter the key (32-byte hexadecimal): ")

    try:
        # Convert the user input to bytes
        key = bytes.fromhex(key_input)
    except ValueError:
        print("Invalid key format. Please enter a valid hexadecimal key.")
        exit()

    input_image_path = '/Users/jeevanprakash/Documents/cyber_project/encrypt/enc50.enc'
    output_image_path = '/Users/jeevanprakash/Documents/cyber_project/decrypt/dec50.jpeg'

    try:
        decrypt_image(input_image_path, output_image_path, key)
    except ValueError as e:
        print(f"Decryption failed: {e}")
