contacts = []
def add_contact():
    name = input("Enter contact name: ")
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print("Contact with this name already exists.")
            return   
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact = (name, phone_number, email)
    contacts.append(contact)
    print(f"Contact for {name} added successfully.")
def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nAll Contacts:")
        for contact in contacts:
            print(f"Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
def search_contact():
    name = input("Enter the name of the contact you want to search : ")
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print(f"Contact Found - Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
            return
    print("Contact not found.")
def update_phone_number():
    name = input("Enter the name of the contact you want to update: ")
    for i, contact in enumerate(contacts):
        if contact[0].lower() == name.lower():
            new_phone_number = input("Enter the new phone number: ")
            contacts[i] = (contact[0], new_phone_number, contact[2])
            print(f"Phone number for {name} updated successfully.")
            return
    print("Contact not found.")
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    for i, contact in enumerate(contacts):
        if contact[0].lower() == name.lower():
            del contacts[i]
            print(f"Contact for {name} deleted successfully.")
            return
    print("Contact not found.")
def menu():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add a New Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact by Name")
        print("4. Update a Contact’s Phone Number")
        print("5. Delete a Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_phone_number()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
