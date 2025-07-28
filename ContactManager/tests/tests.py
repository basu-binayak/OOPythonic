from Classes import Contact, Friend, Supplier

def test_Contact():
    c1 = Contact("Alice", "alice@example.com")
    c2 = Contact("Bob", "bob@example.com")
    c3 = Contact("Alice Baby", "alicebaby@example.com")

    print(Contact.all_contacts)
    # Output:
    # [Contact('Alice', 'alice@example.com'), Contact('Bob', 'bob@example.com')]
    
    print([c.name for c in Contact.all_contacts.search("Alice")])
    
def test_Friend():
    f = Friend("Dusty", "Dusty@private.com", "555-1212")
    print(Contact.all_contacts)
    f.contact()