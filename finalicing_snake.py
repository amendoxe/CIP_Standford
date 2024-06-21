"""So I'm gonna work here, and constantly copy pasting because it might be easier"""

import time
import random
from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.2


def clear_canvas(canvas):
    """Clear all Canvas"""
    canvas.clear()


def start_game(canvas):
    """Check if Enter was pressed to start the game"""
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
    canvas.create_rectangle(0, 0, CANVAS_HEIGHT, CANVAS_WIDTH, color="brown")

    canvas.create_rectangle(0, 0, CANVAS_HEIGHT, CANVAS_WIDTH, color="cyan")

    x_point_three = CANVAS_WIDTH * 0.3
    x_point_four = CANVAS_WIDTH * 0.4
    y_center = CANVAS_HEIGHT / 2
    y_third = CANVAS_HEIGHT / 3
    canvas.create_text(
        x_point_three, y_third, text="CODE IN PLACE, SNAKE GAME", color="orange"
    )
    canvas.create_text(
        x_point_four, y_center, text="Press Enter to play!", color="green"
    )


def main():
    """main program"""
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # Starting the game
    start_screen(canvas)
    start_game(canvas)
    clear_canvas(canvas)

    # actual game
    snake_path = []
    player_list = create_player(canvas)  # create player
    goal, goal_position = create_goal(canvas)  # create goal
    # tryinig appending first
    player_list.append(create_block(canvas, [0, 0, SIZE, SIZE]))  # add to snake body

    direction = "right"
    time.sleep(DELAY)
    # go_right(canvas, player_list, direction, goal, goal_position, snake_path)
    move_snake(canvas, player_list, direction, goal, goal_position, snake_path)


def move_snake(canvas, player_list, direction, goal, goal_position, snake_path):
    """move snake in the initial direction"""

    while True:  # check current direction
        snake_length = len(player_list)
        player = player_list[0]
        x, y = canvas.coords(player)  # obtener las coordenadas iniciales
        x_limit = CANVAS_WIDTH - SIZE
        y_limit = CANVAS_HEIGHT - SIZE
        if direction == "right":
            x += SIZE
        elif direction == "left":
            x -= SIZE
        elif direction == "up":
            y -= SIZE
        elif direction == "down":
            y += SIZE
        canvas.moveto(player, x, y)  # actual movement
        # check if snake is out of bounds
        if x < 0 or x > x_limit:
            break
        if y < 0 or y > y_limit:
            break
        snake_path.insert(0, (x, y))  # saving movement to list

        """ if snake_length ==2:
            canvas.moveto(player_list[0] , snake_path[0][0], snake_path[0][1])
        """
        for i in range(1, snake_length):
            canvas.moveto(player_list[i], snake_path[i - 1][0], snake_path[i - 1][1])
        time.sleep(DELAY)

        collision = collision_check(canvas, player, snake_length)  # Check collision
        if collision:
            canvas.delete(goal)

            # new_snake_block = create_block(canvas, goal_position)  # position of taken goal

            player_list.append(create_block(canvas, goal_position))  # add to snake body

            # print("Appending to snake", new_snake_block)

            # delete old goal and creates a new one
            # canvas.delete(goal)
            goal, goal_position = create_goal(canvas)
            collision = False

        # revisar la direccion direction
        # si la direccion es diferente de "ArrowRight", break
        # move player, en la direccion de direction
        direction = choose_direction(canvas, direction)  # ARROW Press
        if direction == None:
            break

    end_game(canvas, player_list)


def choose_direction(canvas, direction):
    """
    Takes the user input(right, up, left or right)
    and animates the movement in that direction
    """
    key = canvas.get_last_key_press()
    if key == "ArrowLeft":
        return "left"
    elif key == "ArrowRight":
        return "right"
    elif key == "ArrowUp":
        return "up"
    elif key == "ArrowDown":
        return "down"
    else:
        return direction


def collision_check(canvas, player, snake_length):  # check for overlapping objects
    """If theres any overlapping returns True"""
    player_left_x = canvas.get_left_x(player)  # player coordinantes
    player_top_y = canvas.get_top_y(player)
    player_right_x = player_left_x + SIZE
    player_bottom_y = player_top_y + SIZE

    overlapping_objects = canvas.find_overlapping(
        player_left_x, player_top_y, player_right_x, player_bottom_y
    )
    print("overlapping objects:", overlapping_objects)
    overlapping_length = len(overlapping_objects)
    if snake_length == 1:  # first run
        print("first run snake lenght 1, overlaping length", overlapping_length)
        if overlapping_length > 1:
            return True
        else:

            return False
    elif snake_length > 1:
        if overlapping_length - 1 > 1:
            return True
        else:
            return False


def end_game(canvas, player_list):
    """Manages what happens when the game ends"""
    print(len(player_list))
    end_screen(canvas)
    print("You played well")


def end_screen(canvas):
    """
    Create screen hopefully with the result
    """
    clear_canvas(canvas)
    canvas.create_rectangle(0, 0, CANVAS_HEIGHT, CANVAS_WIDTH, color="brown")
    time.sleep(0.1)
    canvas.create_rectangle(0, 0, CANVAS_HEIGHT, CANVAS_WIDTH, color="cyan")

    x_point_three = CANVAS_WIDTH * 0.3
    y_center = CANVAS_HEIGHT / 2
    y_third = CANVAS_HEIGHT / 3
    canvas.create_text(x_point_three, y_third, text="You played well", color="orange")
    canvas.create_text(
        x_point_three, y_center, text="Your score is:(some score)", color="green"
    )
    canvas.create_text(
        x_point_three, y_center + SIZE, text="Press Enter to continue", color="green"
    )
    start_game(canvas)
    main()


def create_player(canvas):
    """Create initial player square"""
    # TODO Regresar una lista
    player = []
    top_x = 0
    top_y = 0
    bottom_x = top_x + SIZE
    bottom_y = top_y + SIZE
    coordinates = [top_x, top_y, bottom_x, bottom_y]
    block = create_block(canvas, coordinates)
    player.append(block)
    # player.append(canvas.create_rectangle(top_x, top_y, bottom_x, bottom_y))
    return player


def create_block(canvas, coordinates):
    """Creates and returns a new block"""

    block = canvas.create_rectangle(
        coordinates[0], coordinates[1], coordinates[2], coordinates[3], outline="pink"
    )
    return block


def create_goal(canvas):
    """Creates a new goal orange block"""
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
