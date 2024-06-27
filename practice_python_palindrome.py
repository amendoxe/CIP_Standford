"""Ask the user for a string and print out whether this string is a
 palindrome or not. (A palindrome is a string that reads the same
 forwards and backwards.)"""


def is_palindrome(word):
    """
    word = string
    take a word and work out if it is a palindrome
    take the len
    for each i change the position of the word and reverse it
    if the reversed word == regular word, return True
    """
    rev_list = ""
    word_length = len(word)
    index = word_length
    for i in range(1, word_length + 1):
        rev_list += word[-i]
        index -= 1
    str(rev_list)
    print(rev_list)

    if rev_list == word:
        return True
    else:
        return False


def ask_user(message):
    """message = string
    ask user for an input with the message, return the string user input"""
    while True:
        user_input = input(message)
        if user_input.isnumeric():
            pass
        else:
            return user_input


def main():
    user_word = ask_user("Write a word to see if it is a palindrome: ")
    if is_palindrome(user_word):
        print("It is in fact a palindrome")
    else:
        print("It is not so much a palindrome, as it is just a word!")


main()
