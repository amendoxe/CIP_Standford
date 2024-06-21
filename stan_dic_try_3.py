def make_dict(list):
    """take the elements from a list and use them as keys in a dictionary
    and use the times that element repeats in the dictionary as values
    make blank dictionary
    iterate the list
    if the number in the list not already on dictionary, add it
    else increase its value
    """
    dict = {}
    for i in range(len(list)):
        # create key with 1 value, if not present
        if list[i] not in dict:
            dict[list[i]] = 1
        else:  # increase value if present
            dict[list[i]] += 1
    print(dict)


def main():
    """Working with list and dictionary"""
    some_list = [4, 4, 4, 2, 4, 5, 5, 1, 6, 8]
    make_dict(some_list)


main()
