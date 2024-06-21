def trace_right_diagonal():
    # pre karel facing east, on the south west corner of map
    # post karel facing east on the south east corner of map
    step_right_beeper()


def step_right_beeper():
    while front_is_clear():
        step_up()
        put_beeper()


def step_up():
    # pre karel facing east
    # post one step above facing east
    move()
    turn_left()
    move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def trace_left_diagonal():
    # pre karel on top left corner facing east
    # if movecheck world is pair, go back one step, then to floor
    # if downcheck world is odd, go straight down
    step_check_down()


def step_check_down():
    while no_beepers_present():
        move()
        if beepers_present():
            back_one_step()
            to_floor()
            mark_center()
        else:
            turn_right()
            move()
            turn_left()
            check_beep_down()


def mark_center():
    # center marked
    put_beeper()


def back_one_step():
    turn_around()
    move()
    turn_around()


def check_beep_down():
    # check on the way down(odd) for beepers
    if beepers_present():
        to_floor()
        mark_center()


def to_floor():
    turn_right()
    to_wall()
    turn_left()


def to_leftside():
    # pre karel on the top right corner facing east
    # post karel on the left top corner facing west
    turn_around()
    to_wall()


def to_wall():
    # move until meeting a wall
    while front_is_clear():
        move()


def turn_around():
    # 180deg turn
    turn_left()
    turn_left()


def clean_other_beeps():
    # pre: facing east
    # post: facing right on starting line position, no beepers on line
    step_up()
    turn_around()
    to_wall()
    turn_around()
    clean_line()


def clean_line():
    # post: ends facing right on starting line position
    while front_is_clear():
        if beepers_present():
            pick_beeper()
            check_move()
        else:
            check_move()
    check_beep()  # fencepost on last beeper
    turn_around()
    to_wall()
    turn_around()


def check_move():
    if front_is_clear():
        move()


def check_beep():
    # pick if theres a beeper
    if beepers_present():
        pick_beeper()


def to_center_beeper():
    # last step of the program ends on center mark
    to_floor()
    while no_beepers_present():
        move()


def main():
    trace_right_diagonal()
    to_leftside()
    turn_around()
    trace_left_diagonal()
    while left_is_clear():
        clean_other_beeps()
    to_center_beeper()
