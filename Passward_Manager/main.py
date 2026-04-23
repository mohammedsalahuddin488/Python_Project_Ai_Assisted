import pyperclip
import os

Filename = "passwords.txt"

def add_password():
    website = input("Enter the website: ")
    password = input("Enter the password: ")
    with open(Filename, 'a') as file:
        file.write(f"{website}: {password}\n")

def view_passwords():
    website = input("Enter the website to view the password: ")
    with open(Filename, 'r') as file:
        for line in file:
            if line.startswith(website + ":"):
                password = line.split(":")[1].strip()
                print(f"Password for {website}: {password}")
                pyperclip.copy(password)
                print("Password copied to clipboard.")
                return
            break
            copy_password = input("Password not found. Do you want to copy the last password to clipboard? (y/n): ")
def main():
    while True:
        print("Password Manager")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

main()