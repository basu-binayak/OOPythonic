from __future__ import annotations
# It tells Python to treat all type annotations as strings, so you can reference a class (Contact) before it’s actually defined.

class ContactList(list["Contact"]):
    # ContactList is a custom class that inherits from the built-in list, but it's meant to hold only Contact objects. list["Contact"] means it’s a list of Contact objects.
    def search(self, name:str) -> list["Contact"]:
        matching_contacts: list["Contact"] = []
        for contact in self:
            # Iterates through the list (self), which is a ContactList, so every item should be a Contact.
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts



class Contact:
    '''
    The Contact class is responsible for maintaining a global list of all contacts ever seen in a class variable, and for initializing the name and address for an individual contact
    '''
    all_contacts = ContactList()  # Class variable that stores all contacts
    
    
    def __init__(self, name:str, email:str):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)  # Add the new contact to the list
    
    def contact(self):
        print(f"Contacting {self.name} via email: {self.email}")
        
    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.name!r} , {self.email!r})"
        )
    # The !r inside a Python f-string is a conversion flag that tells Python to use the repr() representation of the object instead of the usual str() representation.
    '''
        f"{name}" → uses str(name) → prints Alice
        f"{name!r}" → uses repr(name) → prints 'Alice' with quotes

        This is very helpful when debugging or logging, especially with strings — because you can clearly see if there are:
            extra spaces
            missing characters
            invisible characters (like newline \n)
    '''
        

    