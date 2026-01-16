passwords = []

def add_password():
    site = input("Enter website name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    passwords.append({"site": site, "username": username, "password": password})
    print("Password saved")

def view_passwords():
    if not passwords:
        print("No passwords saved")
    else:
        for pwd in passwords:
            print("Site:", pwd["site"], "| Username:", pwd["username"], "| Password:", pwd["password"])

def main():
    while True:
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
