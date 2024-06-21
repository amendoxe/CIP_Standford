    size_the_world()

def size_the_world():
    #count by going up one step
    two()
    if no_beepers_present():
        five()
        if no_beepers_present():
            six()

def two():
    #asume the world is 2x2
    step_up()
    check_two()

def five():
    for i in range(3):
        step_up()
    check_five()


def six():
    step_up()
    check_six()

def check_six():
#for now no check
    step_down()
    down_on_third_column()
    mark_center()

def step_up():
    #pre facing east
    #post end north-east of precondition
    move()
    turn_left()
    move()
    turn_right()
def check_two():
    #if Karel is not facing a wall continue to three
    if front_is_blocked():
        one_step_down()
        mark_center()
    else:
        pass
def check_five():
    #if Karel is not facing a wall continue to four
    if front_is_clear():
        pass
    else:
        down_on_third_column()
        mark_center()
def down_on_third_column():
    step_down()
    step_down()
    column_start()
def column_start():
    #karel ends on the southmost part of the current column
    turn_right()
    to_wall()
    turn_left()
def to_wall():
    while front_is_clear():
        move()
def turn_right():
    #post end facing right of initial position
    for i in range(3):
        turn_left()

def one_step_down():
    step_down()

def step_down():
    #post end south-west position fron initial, facing east
    turn_right()
    move()
    turn_right()
    move()
    turn_around()
def turn_around():
    turn_left()
    turn_left()

def mark_center():
    #place beeper
    put_beeper()
