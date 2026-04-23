import json
import os
import secrets
import string
from cryptography.fernet import Fernet

# Generate or load encryption key (in a real app, store this securely)
KEY_FILE = "key.key"
DATA_FILE = "passwords.enc"

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as file:
            return file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
        return key

def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()

def load_passwords(key):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = decrypt_data(encrypted_data, key)
        return json.loads(decrypted_data)
    return {}

def save_passwords(passwords, key):
    data = json.dumps(passwords)
    encrypted_data = encrypt_data(data, key)
    with open(DATA_FILE, "wb") as file:
        file.write(encrypted_data)

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def add_password(passwords, key):
    website = input("Enter the website: ").strip()
    if not website:
        print("Website cannot be empty.")
        return
    use_generated = input("Generate a strong password? (y/n): ").lower() == 'y'
    if use_generated:
        password = generate_password()
        print(f"Generated password: {password}")
    else:
        password = input("Enter the password: ").strip()
        if not password:
            print("Password cannot be empty.")
            return
    passwords[website] = password
    save_passwords(passwords, key)
    print("Password added successfully.")

def view_passwords(passwords):
    website = input("Enter the website to view the password: ").strip()
    if website in passwords:
        print(f"Password for {website}: {passwords[website]}")
    else:
        print("Password not found.")

def delete_password(passwords, key):
    website = input("Enter the website to delete: ").strip()
    if website in passwords:
        del passwords[website]
        save_passwords(passwords, key)
        print("Password deleted successfully.")
    else:
        print("Password not found.")

def update_password(passwords, key):
    website = input("Enter the website to update: ").strip()
    if website in passwords:
        new_password = input("Enter the new password: ").strip()
        if new_password:
            passwords[website] = new_password
            save_passwords(passwords, key)
            print("Password updated successfully.")
        else:
            print("Password cannot be empty.")
    else:
        print("Password not found.")

def main():
    key = load_key()
    master_password = input("Enter master password: ").strip()
    # In a real app, hash and verify master password securely
    if master_password != "your_master_password":  # Replace with actual check
        print("Incorrect master password.")
        return
    
    passwords = load_passwords(key)
    
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Password")
        print("3. Delete Password")
        print("4. Update Password")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_password(passwords, key)
        elif choice == '2':
            view_passwords(passwords)
        elif choice == '3':
            delete_password(passwords, key)
        elif choice == '4':
            update_password(passwords, key)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    