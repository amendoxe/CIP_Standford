"""
practice_python_divisors.py
-------------------------------
Create a program that asks the user for a number and then
prints out a list of all the divisors of that number.
"""


def ask_user(message):
    """ask for message input and return an integer"""
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            pass


def check_number(x):
    """check the dividends of x and print them"""
    print([i for i in range(1, x + 1) if x % i == 0])


def main():
    """main"""
    number_to_check = ask_user("which number, you want to check? ")
    check_number(number_to_check)


main()
