# contact_book.py
contacts = {}

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
    elif choice == "2":
        name = input("Enter name to search: ")
        print(contacts.get(name, "Contact not found"))
    elif choice == "3":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Deleted")
        else:
            print("Contact not found")
    elif choice == "4":
        break
    else:
        print("Invalid choice")