"""So I'm gonna work here, and constantly copy pasting because it might be easier"""

from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1


def set_background(canvas):
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, color="green")


def clear_canvas(canvas):
    canvas.clear()


def start_game(canvas):
    # When Enter is pressed start game
    while True:
        key = canvas.get_last_key_press()
        print(key)
        time.sleep(0.4)
        if key == "Enter":
            break


def start_screen(canvas):
    """
    Create a starting screen with title and instruction to start
    """
    backbround = canvas.create_rectangle(
        0, 0, CANVAS_HEIGHT, CANVAS_WIDTH, color="brown"
    )

    backbround = canvas.create_rectangle(
        0, 0, CANVAS_HEIGHT, CANVAS_WIDTH, color="cyan"
    )

    x_point_three = CANVAS_WIDTH * 0.3
    x_point_four = CANVAS_WIDTH * 0.4
    y_center = CANVAS_HEIGHT / 2
    y_third = CANVAS_HEIGHT / 3
    title = canvas.create_text(
        x_point_three, y_third, text="CODE IN PLACE, SNAKE GAME", color="orange"
    )
    enter_to_play = canvas.create_text(
        x_point_four, y_center, text="Press Enter to play!", color="green"
    )


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # Starting the game
    start_screen(canvas)
    start_game(canvas)
    clear_canvas(canvas)

    # actual game
    # TODO hacer de player una lista
    player = create_player(canvas)  # create player
    goal, goal_position = create_goal(canvas)  # create goal
    direction = "right"
    time.sleep(DELAY)
    go_right(canvas, player, direction, goal, goal_position)


def choose_direction(canvas, direction):
    """
    Takes the user input(right, up, left or right)
    and animates the movement in that direction
    """
    key = canvas.get_last_key_press()
    if key == "ArrowLeft":
        # print('left arrow pressed!')
        return "left"
    if key == "ArrowRight":
        # print('right arrow pressed!')
        return "right"
    if key == "ArrowUp":
        # print('up arrow pressed!')
        return "up"
    if key == "ArrowDown":
        # print('down arrow pressed!')
        return "down"
    if key == None:
        return direction


def go_right(canvas, player, direction, goal, goal_position):
    # direction is the current facing direction
    # TODO de la lista player mover el primero?
    # TODO intentar mover la lista, append en if colission
    x = canvas.get_left_x(player)
    y = canvas.get_top_y(player)
    x_limit = CANVAS_WIDTH - SIZE
    while x < x_limit:
        x += SIZE
        canvas.moveto(player, x, y)  # MOVE
        time.sleep(DELAY)
        colission = colission_check(canvas, player)  # Check colission
        if colission:
            # TODO pass the goal position to append snake
            new_snake_block = goal_position  # position of taken goal
            print("Appending to snake", new_snake_block)
            canvas.delete(goal)
            goal, goal_position = create_goal(canvas)

        # revisar la direccion direction
        # si la direccion es diferente de "ArrowRight", break
        # move player, en la direccion de direction
        direction = choose_direction(canvas, direction)  # ARROW Press
        # print("curren direction is ", direction)
        if direction == "right":
            continue
        else:
            break
    if direction == "left":
        go_left(canvas, player, direction, goal, goal_position)
    elif direction == "up":
        go_up(canvas, player, direction, goal, goal_position)
    elif direction == "down":
        go_down(canvas, player, direction, goal, goal_position)
    end_game(canvas)


def go_left(canvas, player, direction, goal, goal_position):
    x = canvas.get_left_x(player)
    y = canvas.get_top_y(player)
    x_limit = 0
    while x > x_limit:
        x -= SIZE
        canvas.moveto(player, x, y)
        time.sleep(DELAY)
        colission = colission_check(canvas, player)  # Check colission
        if colission:
            new_snake_block = goal_position  # position of taken goal
            print("Appending to snake", new_snake_block)
            canvas.delete(goal)
            goal, goal_position = create_goal(canvas)

        # revisar la direccion direction
        # si la direccion es diferente de "ArrowRight", break
        # move player, en la direccion de direction
        direction = choose_direction(canvas, direction)
        if direction != "left":
            break
    if direction == "right":
        go_right(canvas, player, direction, goal, goal_position)
    elif direction == "up":
        go_up(canvas, player, direction, goal, goal_position)
    elif direction == "down":
        go_down(canvas, player, direction, goal, goal_position)


def go_down(canvas, player, direction, goal, goal_position):
    x = canvas.get_left_x(player)
    y = canvas.get_top_y(player)
    y_limit = CANVAS_HEIGHT - SIZE
    while y < y_limit:
        y += SIZE
        canvas.moveto(player, x, y)
        time.sleep(DELAY)
        colission = colission_check(canvas, player)  # Check colission
        if colission:
            new_snake_block = goal_position  # position of taken goal
            print("Appending to snake", new_snake_block)
            canvas.delete(goal)
            goal, goal_position = create_goal(canvas)
        # revisar la direccion direction
        # si la direccion es diferente de "ArrowRight", break
        # move player, en la direccion de direction
        direction = choose_direction(canvas, direction)
        if direction != "down":
            delete_goal(canvas)
            break
    if direction == "right":
        go_right(canvas, player, direction, goal, goal_position)
    elif direction == "up":
        go_up(canvas, player, direction, goal, goal_position)
    elif direction == "left":
        go_left(canvas, player, direction, goal, goal_position)


def go_up(canvas, player, direction, goal, goal_position):
    x = canvas.get_left_x(player)
    y = canvas.get_top_y(player)
    y_limit = 0
    while y > y_limit:
        y -= SIZE
        canvas.moveto(player, x, y)
        time.sleep(DELAY)
        colission = colission_check(canvas, player)  # Check colission
        if colission:
            new_snake_block = goal_position  # position of taken goal
            print("Appending to snake", new_snake_block)
            canvas.delete(goal)
            goal, goal_position = create_goal(canvas)
        # revisar la direccion direction
        # si la direccion es diferente de "ArrowRight", break
        # move player, en la direccion de direction
        direction = choose_direction(canvas, direction)
        if direction != "up":
            break
    if direction == "right":
        go_right(canvas, player, direction, goal, goal_position)
    elif direction == "left":
        go_left(canvas, player, direction, goal, goal_position)
    elif direction == "down":
        go_down(canvas, player, direction, goal, goal_position)


def delete_goal(canvas):
    pass


def colission_check(canvas, player):  # check for overlapping objects
    player_left_x = canvas.get_left_x(player)  # player coordenates
    player_top_y = canvas.get_top_y(player)
    player_right_x = player_left_x + SIZE
    player_bottom_y = player_top_y + SIZE

    overlapping_objects = canvas.find_overlapping(
        player_left_x, player_top_y, player_right_x, player_bottom_y
    )
    # print("The overlapping objects are:", overlapping_objects)
    overlaping_length = len(overlapping_objects)
    if overlaping_length > 1:
        return True
    # TODO return the goal position
    else:
        return False


def end_game(canvas):
    end_screen(canvas)
    print("You played well")


def end_screen(canvas):
    """
    Create screen hopefully with the result
    """
    clear_canvas(canvas)
    backbround = canvas.create_rectangle(
        0, 0, CANVAS_HEIGHT, CANVAS_WIDTH, color="brown"
    )
    time.sleep(0.1)
    backbround = canvas.create_rectangle(
        0, 0, CANVAS_HEIGHT, CANVAS_WIDTH, color="cyan"
    )

    x_point_three = CANVAS_WIDTH * 0.3
    x_point_four = CANVAS_WIDTH * 0.4
    y_center = CANVAS_HEIGHT / 2
    y_third = CANVAS_HEIGHT / 3
    cheering = canvas.create_text(
        x_point_three, y_third, text="You played well", color="orange"
    )
    score_display = canvas.create_text(
        x_point_three, y_center, text="Your score is:(some score)", color="green"
    )
    enter_to_play = canvas.create_text(
        x_point_three, y_center + SIZE, text="Press Enter to continue", color="green"
    )
    start_game(canvas)
    main()


def create_player(canvas):
    # Create the black square
    # TODO Regresar una lista
    top_x = 0
    top_y = 0
    bottom_x = top_x + SIZE
    bottom_y = top_y + SIZE
    return canvas.create_rectangle(top_x, top_y, bottom_x, bottom_y)


def create_goal(canvas):
    # Create the orange square
    top_x = random.randint(0, 19) * 20
    top_y = random.randint(0, 19) * 20
    bottom_x = top_x + SIZE
    bottom_y = top_y + SIZE
    goal_position = [top_x, top_y, bottom_x, bottom_y]
    return (
        canvas.create_rectangle(top_x, top_y, bottom_x, bottom_y, color="orange"),
        goal_position,
    )


if __name__ == "__main__":
    main()
