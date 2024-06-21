def add_contact(contacts, name, number, birthday=None, email=None):
    """
    builds a contact based on the given info and then adds it to contacts
    params:
        name (str): name of the contact
        number (str): phone number of the contact
        birthday (str or None): birthday of the contact (optional)
        email (str or None): email of the contact (optional)
    """
    contact = {"number": number}

    # birthday and email are 'optional' arguments because they have
    # default values, but we don't want None in our contacts dict
    if birthday != None:
        contact["birthday"] = birthday

    if email != None:
        contact["email"] = email

    contacts[name] = contact
    # notice how we don't return contact


def main():
    contacts = {}

    # add the three contacts using our helper function
    add_contact(contacts, "Kiera", "337-8520", "2 March", "kgomez4@gmail.com")
    add_contact(contacts, "Stefan", "738-7216", "24 July")
    add_contact(contacts, "Jasmin", "755-8090", email="jas.shah@gmail.com")

    print(contacts)


main()
