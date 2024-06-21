"""So I'm gonna work here, and constantly copy pasting because it might be easier"""

import time
import random
from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1


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
    direction = "right"
    time.sleep(DELAY)
    go_right(canvas, player_list, direction, goal, goal_position, snake_path)


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


def go_right(canvas, player_list, direction, goal, goal_position, snake_path):
    """
    direction is the current facing direction
    """
    snake_length = len(player_list)
    # pre_x, pre_y = canvas.coords(player_list[i - 1])

    # TODO intentar mover la lista, append en if collision
    player = player_list[0]
    x = canvas.get_left_x(player)
    y = canvas.get_top_y(player)
    x_limit = CANVAS_WIDTH - SIZE
    while x < x_limit:
        x += SIZE
        canvas.moveto(player, x, y)  # Actually moving
        snake_path.append(canvas.coords(player))
        print(snake_path)
        # provando
        if snake_length > 1:  # If there's more than one square
            for i in range(1, snake_length):  # move to previous i coordinates
                pre_x, pre_y = snake_path[-i]
                canvas.moveto(player_list[i], pre_x, pre_y)

        # provando

        """if snake_length > 1:  # If there's more than one square
            for i in range(1, snake_length):  # move to previous i coordinates
                canvas.moveto(player_list[i], x - SIZE, y)"""

        time.sleep(DELAY)
        collision = collision_check(canvas, player)  # Check collision
        if collision:
            # TODO pass the goal position to append snake
            new_snake_block = create_block(
                canvas, goal_position
            )  # position of taken goal
            # appending
            canvas.set_color(new_snake_block, color="black")
            player_list.append(new_snake_block)
            print("Appending to snake", new_snake_block)
            # delete old goal and creates a new one
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
        go_left(canvas, player_list, direction, goal, goal_position, snake_path)
    elif direction == "up":
        go_up(canvas, player_list, direction, goal, goal_position, snake_path)
    elif direction == "down":
        go_down(canvas, player_list, direction, goal, goal_position, snake_path)
    end_game(canvas, player_list)


def go_left(canvas, player_list, direction, goal, goal_position, snake_path):
    """move snake to the left"""
    snake_length = len(player_list)

    player = player_list[0]
    x = canvas.get_left_x(player)
    y = canvas.get_top_y(player)
    x_limit = 0
    while x > x_limit:
        x -= SIZE
        canvas.moveto(player, x, y)  # Actually moving

        snake_path.append(canvas.coords(player))
        print(snake_path)

        # provando
        if snake_length > 1:  # If there's more than one square
            for i in range(1, snake_length):  # move to previous i coordinates
                pre_x, pre_y = snake_path[-i]
                canvas.moveto(player_list[i], pre_x, pre_y)
        # provando

        """if snake_length > 1:  # If there's more than one square
            for i in range(1, snake_length):  # move to previous i coordinates
                canvas.moveto(player_list[i], x + SIZE, y)"""

        time.sleep(DELAY)
        collision = collision_check(canvas, player)  # Check collision
        if collision:
            # TODO pass the goal position to append snake
            new_snake_block = create_block(
                canvas, goal_position
            )  # position of taken goal
            # appending
            canvas.set_color(new_snake_block, color="black")
            player_list.append(new_snake_block)
            print("Appending to snake", new_snake_block)
            # delete old goal and creates a new one
            canvas.delete(goal)
            goal, goal_position = create_goal(canvas)

        # revisar la direccion direction
        # si la direccion es diferente de "ArrowRight", break
        # move player, en la direccion de direction
        direction = choose_direction(canvas, direction)
        if direction != "left":
            break
    if direction == "right":
        go_right(canvas, player_list, direction, goal, goal_position, snake_path)
    elif direction == "up":
        go_up(canvas, player_list, direction, goal, goal_position, snake_path)
    elif direction == "down":
        go_down(canvas, player_list, direction, goal, goal_position, snake_path)
    end_game(canvas, player_list)


def go_down(canvas, player_list, direction, goal, goal_position, snake_path):
    """move snake down"""
    snake_length = len(player_list)

    player = player_list[0]
    x = canvas.get_left_x(player)
    y = canvas.get_top_y(player)
    y_limit = CANVAS_HEIGHT - SIZE
    while y < y_limit:
        y += SIZE
        canvas.moveto(player, x, y)  # Actually moving

        snake_path.append(canvas.coords(player))
        print(snake_path)

        # provando
        if snake_length > 1:  # If there's more than one square
            for i in range(1, snake_length):  # move to previous i coordinates
                pre_x, pre_y = snake_path[-i]
                canvas.moveto(player_list[i], pre_x, pre_y)
        # provando

        """if snake_length > 1:  # If there's more than one square
            for i in range(1, snake_length):  # move to previous i coordinates
                canvas.moveto(player_list[i], x, y - SIZE)"""

        time.sleep(DELAY)
        collision = collision_check(canvas, player)  # Check collision
        if collision:
            # TODO pass the goal position to append snake
            new_snake_block = create_block(
                canvas, goal_position
            )  # position of taken goal
            # appending
            canvas.set_color(new_snake_block, color="black")
            player_list.append(new_snake_block)
            print("Appending to snake", new_snake_block)
            # delete old goal and creates a new one

            canvas.delete(goal)
            goal, goal_position = create_goal(canvas)
        # revisar la direccion direction
        # si la direccion es diferente de "ArrowRight", break
        # move player, en la direccion de direction
        direction = choose_direction(canvas, direction)
        if direction != "down":
            break
    if direction == "right":
        go_right(canvas, player_list, direction, goal, goal_position, snake_path)
    elif direction == "up":
        go_up(canvas, player_list, direction, goal, goal_position, snake_path)
    elif direction == "left":
        go_left(canvas, player_list, direction, goal, goal_position, snake_path)
    end_game(canvas, player_list)


def go_up(canvas, player_list, direction, goal, goal_position, snake_path):
    """move snake up"""
    snake_length = len(player_list)

    player = player_list[0]
    x = canvas.get_left_x(player)
    y = canvas.get_top_y(player)
    y_limit = 0
    while y > y_limit:
        y -= SIZE
        canvas.moveto(player, x, y)  # Actually moving

        snake_path.append(canvas.coords(player))
        print(snake_path)

        # provando
        if snake_length > 1:  # If there's more than one square
            for i in range(1, snake_length):  # move to previous i coordinates
                pre_x, pre_y = snake_path[-i]
                canvas.moveto(player_list[i], pre_x, pre_y)
        # provando

        """if snake_length > 1:  # If there's more than one square
            for i in range(1, snake_length):  # move to previous i coordinates
                canvas.moveto(player_list[i], x, y + SIZE)"""

        time.sleep(DELAY)
        collision = collision_check(canvas, player)  # Check collision
        if collision:
            # TODO pass the goal position to append snake
            new_snake_block = create_block(
                canvas, goal_position
            )  # position of taken goal
            # appending
            canvas.set_color(new_snake_block, color="black")
            player_list.append(new_snake_block)
            print("Appending to snake", new_snake_block)
            # delete old goal and creates a new one
            canvas.delete(goal)
            goal, goal_position = create_goal(canvas)
        # revisar la direccion direction
        # si la direccion es diferente de "ArrowRight", break
        # move player, en la direccion de direction
        direction = choose_direction(canvas, direction)
        if direction != "up":
            break
    if direction == "right":
        go_right(canvas, player_list, direction, goal, goal_position, snake_path)
    elif direction == "left":
        go_left(canvas, player_list, direction, goal, goal_position, snake_path)
    elif direction == "down":
        go_down(canvas, player_list, direction, goal, goal_position, snake_path)
    end_game(canvas, player_list)


def collision_check(canvas, player):  # check for overlapping objects
    """If theres any overlapping returns True"""
    player_left_x = canvas.get_left_x(player)  # player coordinantes
    player_top_y = canvas.get_top_y(player)
    player_right_x = player_left_x + SIZE
    player_bottom_y = player_top_y + SIZE

    overlapping_objects = canvas.find_overlapping(
        player_left_x, player_top_y, player_right_x, player_bottom_y
    )
    overlapping_length = len(overlapping_objects)
    if overlapping_length > 1:
        return True
    # TODO return the goal position
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
        coordinates[0], coordinates[1], coordinates[2], coordinates[3]
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
