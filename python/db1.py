# List to store password entries
passwords = []

# Function to add a password entry
def add_password():
    website = input("Enter website/application name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    entry = {
        "website": website,
        "username": username,
        "password": password
    }
    passwords.append(entry)
    print(f"Added password entry for {website}.")

# Function to view all password entries
def view_passwords():
    if passwords:
        print("\n--- Password Entries ---")
        for index, entry in enumerate(passwords, start=1):
            print(f"{index}. Website: {entry['website']}, Username: {entry['username']}, Password: {entry['password']}")
    else:
        print("No password entries found.")

# Function to update a password entry
def update_password():
    view_passwords()
    if passwords:
        try:
            index = int(input("Enter the number of the entry to update: ")) - 1
            if 0 <= index < len(passwords):
                website = input(f"Enter new website name ({passwords[index]['website']}): ") or passwords[index]['website']
                username = input(f"Enter new username ({passwords[index]['username']}): ") or passwords[index]['username']
                password = input(f"Enter new password ({passwords[index]['password']}): ") or passwords[index]['password']
                passwords[index] = {
                    "website": website,
                    "username": username,
                    "password": password
                }
                print(f"Updated password entry for {website}.")
            else:
                print("Invalid entry number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No password entries to update.")

# Function to delete a password entry
def delete_password():
    view_passwords()
    if passwords:
        try:
            index = int(input("Enter the number of the entry to delete: ")) - 1
            if 0 <= index < len(passwords):
                deleted_entry = passwords.pop(index)
                print(f"Deleted password entry for {deleted_entry['website']}.")
            else:
                print("Invalid entry number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No password entries to delete.")

# Main menu
def main():
    while True:
        print("\n--- Password Management System ---")
        print("1. Add Password Entry")
        print("2. View Password Entries")
        print("3. Update Password Entry")
        print("4. Delete Password Entry")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            update_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()