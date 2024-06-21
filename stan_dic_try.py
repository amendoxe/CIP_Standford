def main():
    dictionary_1 = {}
    phones = {"pat": 33143124, "Juliette": 924379, "Mehran": 4293879, "Chris": 7236532}
    if dictionary_1:
        print("First, true")
    else:
        print("First, false")

    print(phones["Chris"], phones["Juliette"])
    print(phones["pat"], phones["Mehran"])

    for key in phones:
        some_variable = phones[key]
        print("for the iterations", key, "the value is", some_variable)

    print("Creating a list...")
    print(phones.keys())
    list_o_users = phones.keys()
    print(list_o_users)

    for key in phones.keys():
        print(phones.keys())


main()
