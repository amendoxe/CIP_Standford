def make_dict(list):
    """make the list element into the key for a dictionary"""
    my_dict = {}
    for i in range(len(list)):
        num = list[i]
        if num not in my_dict:  # add key
            my_dict[num] = 1
        else:  # increase value
            my_dict[num] += 1

    return my_dict


def make_list(dictionary):
    new_list = list(dictionary.keys())
    second_new_list = list(dictionary.values())
    third_new_list = list(dictionary.items())
    print(new_list)
    print(second_new_list)
    print(third_new_list)


def main():
    """Lets try makin a dictionary from a list"""
    my_list = [5, 1, 3, 6, 8, 5, 3, 3, 3]
    my_dict = make_dict(my_list)
    print("This is my dictionary:/n", my_dict)
    print("My dictionary value for 3 is:", my_dict.get(3))
    make_list(my_dict)


main()
