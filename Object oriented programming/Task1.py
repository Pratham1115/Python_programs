# Mini Project => creating a PhoneBook

class PhoneBook:

    contacts = []

    def __init__(self ,name, phone_number):
        self.name = name
        self.phone_number = phone_number
        PhoneBook.contacts.append(self)

    def show_contacts(self):
        print(f"Name: {self.name} , Phone Number: {self.phone_number}")
    
    @classmethod
    def show_all_contacts(cls):
        if len(cls.contacts) == 0:
            print("No contacts found.")
        else:
            for contact in cls.contacts:
                print(f"Name: {contact.name} , Phone Number: {contact.phone_number}")

    @classmethod
    def search_contact(cls, search_name):
        for contacts in cls.contacts:
            if contacts.name.lower() == name.lower():
                print(contacts.show_contacts())
            else:
                print("Contact not found.")

            
while True:
    ch=int(input('''
    1. Add Contact
    2. Show All Contacts
    3. Search for a contact
    4. Exit'''))
    if ch==1:
        name=input("Enter the name: ")
        phone_number=input("Enter the phone number: ")
        contact=PhoneBook(name,phone_number)

    elif ch==2:
        PhoneBook.show_all_contacts()
    
    elif ch==3:
        PhoneBook.search_contact(input("Enter the name to search: "))

    elif ch==4:
        print("Exiting the program.")
        break   


    
    



    
        