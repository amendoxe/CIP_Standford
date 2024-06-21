def main():
    """ "return double in each list values"""
    list_1 = [1, 2, 3]  # expected output: 2,4,6

    for i, v in enumerate(list_1):
        list_1[i] *= 2
    print(list_1)


main()
