# Function to display all contacts
def display_contacts(contacts):
    if len(contacts) == 0:
        print("Your contact book is empty.")
    else:
        print("Contacts List:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"Contact for {name} added successfully!")

# Function to update an existing contact
def update_contact(contacts):
    display_contacts(contacts)
    if len(contacts) > 0:
        try:
            contact_number = int(input("Enter the number of the contact to update: "))
            if 1 <= contact_number <= len(contacts):
                contact = contacts[contact_number - 1]
                print(f"Updating contact for {contact['name']}")
                contact['name'] = input("Enter new name: ") or contact['name']
                contact['phone'] = input("Enter new phone number: ") or contact['phone']
                contact['email'] = input("Enter new email: ") or contact['email']
                print("Contact updated successfully!")
            else:
                print("Invalid contact number!")
        except ValueError:
            print("Please enter a valid number.")

# Function to delete a contact
def delete_contact(contacts):
    display_contacts(contacts)
    if len(contacts) > 0:
        try:
            contact_number = int(input("Enter the number of the contact to delete: "))
            if 1 <= contact_number <= len(contacts):
                removed_contact = contacts.pop(contact_number - 1)
                print(f"Contact for {removed_contact['name']} deleted successfully!")
            else:
                print("Invalid contact number!")
        except ValueError:
            print("Please enter a valid number.")

# Main program
def contact_book():
    contacts = []
    
    while True:
        print("\nContact Book Menu:")
        print("1. View contacts")
        print("2. Add contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the contact book program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run the program
if __name__ == "__main__":
    contact_book()
