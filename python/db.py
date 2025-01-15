# List to store contacts
contacts = []

# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    address = input("Enter address (optional, press Enter to skip): ")
    contact = {
        "name": name,
        "phone": phone,
        "address": address if address else None
    }
    contacts.append(contact)
    print(f"Added {name} to contacts.")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("\n--- Contacts ---")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Address: {contact['address']}")
    else:
        print("No contacts found.")

# Function to update a contact
def update_contact():
    view_contacts()
    if contacts:
        try:
            index = int(input("Enter the number of the contact to update: ")) - 1
            if 0 <= index < len(contacts):
                name = input(f"Enter new name ({contacts[index]['name']}): ") or contacts[index]['name']
                phone = input(f"Enter new phone number ({contacts[index]['phone']}): ") or contacts[index]['phone']
                address = input(f"Enter new address ({contacts[index]['address']}): ") or contacts[index]['address']
                contacts[index] = {
                    "name": name,
                    "phone": phone,
                    "address": address
                }
                print(f"Updated contact {index + 1}.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No contacts to update.")

# Function to delete a contact
def delete_contact():
    view_contacts()
    if contacts:
        try:
            index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= index < len(contacts):
                deleted_contact = contacts.pop(index)
                print(f"Deleted {deleted_contact['name']} from contacts.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No contacts to delete.")

# Main menu
def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()