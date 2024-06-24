a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for element in a:
    if element < 5:
        b.append(element)
print([element for element in a if element < 5])

"""Ask for a number and make a list of all numbers bellow it"""


def ask_number():
    while True:
        try:
            user_number = int(input("Which number do you want to check? "))
            return user_number
        except ValueError:
            pass


def main():
    b.clear()
    number = ask_number()
    print(f"The list of numbers bellow {number}, is:")
    for element in a:
        if element < number:
            b.append(element)
    print(b)


main()
