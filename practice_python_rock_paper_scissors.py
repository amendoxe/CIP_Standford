"""Rock, paper, scissors game"""


def get_input():
    while True:
        user_input = input("Choose 'r' for rock,'p' for paper or 's'"
                           "for scissors: ")


def generate_hand():
    pass


def main():
    while True:
        user_hand = get_input()
        computer_hand = generate_hand()
        winner = check_hands(user_hand, computer_hand)
        print(f"The winner is {winner}")


main()
