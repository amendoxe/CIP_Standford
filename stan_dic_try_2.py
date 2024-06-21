def main():
    values_list = [3, 5, 1, 3, 1, 5, 4]
    make_dict(values_list)


def make_dict(list):
    """
    from a list create a dictionary with the list element as key and the
    number of times it repeats itself as the value
    """
    my_dict = {}
    for i in range(len(list)):
        if list[i] not in my_dict:
            my_dict[list[i]] = 1
        else:
            my_dict[list[i]] += 1
    print(my_dict)


main()
