class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        if len(self.contacts) >= 100:
            print("Phonebook is full.")
            return
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        self.contacts.append(Contact(name, phone, email))
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
            return
        print("\n--- Phonebook Contacts ---")
        for i, contact in enumerate(self.contacts, 1):
            print(f"Contact {i}:")
            print(f"Name: {contact.name}")
            print(f"Phone: {contact.phone}")
            print(f"Email: {contact.email}")
        print()

    def modify_contact(self):
        name = input("Enter the name of the contact to modify: ")
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                print("Contact modified successfully.")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def menu(self):
        while True:
            print("\n--- Phonebook Menu ---")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Modify Contact")
            print("4. Delete Contact")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.modify_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                print("Exiting phonebook...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    phonebook = Phonebook()
    phonebook.menu()
