import os

def main():
    print("Choose an option:")
    print("1. Encrypt an image")
    print("2. Decrypt an image")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        encrypt_image()
    elif choice == '2':
        decrypt_image()
    else:
        print("Invalid choice. Please enter 1 or 2.")

def encrypt_image():
    # Call the encryption script without passing specific parameters
    os.system("python encrypt.py")

def decrypt_image():
    # Call the decryption script without passing specific parameters
    os.system("python decrypt.py")

if __name__ == "__main__":
    while True:
        main()