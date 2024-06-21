def main():
    # counting I suppose
    what_is()
    reaction()


# if it ends in beeper it is odd, face south
# if it ends empty is pair, face north
def what_is():
    fill_pattern()
    check_last()


# starts on far west corner facing east
# ends far east corner facint east
def fill_pattern():
    while front_is_clear():
        put_beeper()
        if front_is_clear():
            move_check()
            move_check()


# check for a wall for movement while fill_pattern()
def move_check():
    if front_is_clear():
        move()


# if theres beeper (odd) face south
# if ends empty (pair) face north
def check_last():
    if beepers_present():
        turn_right()
    else:
        turn_left()


# ends looking to the right of current direction
def turn_right():
    for i in range(3):
        turn_left()


# based on the position (up or down), react
def reaction():
    if facing_north():  # pair
        clean_except_left()
    else:
        clean_except_middle()  # odd


# Karel is facint north, one the middle left beeper should be left(no pun intended)
def clean_except_left():
    turn_left()
    cleaning_pair()


def clean_except_middle():
    pass


# pick up unused beepers, ends facing west
def cleaning_pair():
    while front_is_clear():
        if beepers_present():
            pick_beeper()
            move()
        move()
    pick_beeper()  # fencepost problem
    check_end()


def cheat_end():
    move()
    put_beeper()


# Karel is facing east on the second corner
# finish 2x2


def second_cheat():
    turn_around()
    move()
    put_beeper()
    turn_around()


# 180deg turn
def turn_around():
    turn_left()
    turn_left()


# karel is facing west
def check_end():
    turn_around()
    move()
    if front_is_clear():
        cheat_end()
    else:
        second_cheat()
