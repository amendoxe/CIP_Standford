import time
import random
from graphics import Canvas  # Assuming graphics library like pygame or tkinter Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 0.1


def clear_canvas(canvas):
    canvas.clear()


def start_game(canvas):
    while True:
        key = canvas.get_last_key_press()
        time.sleep(0.4)
        if key == "Enter":
            break


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    start_game(canvas)
    clear_canvas(canvas)

    snake_path = []
    player_list = create_player(canvas)
    goal, goal_position = create_goal(canvas)
    direction = "right"
    time.sleep(DELAY)
    move_snake(canvas, player_list, direction, goal, goal_position, snake_path)


def move_snake(canvas, player_list, direction, goal, goal_position, snake_path):
    while True:
        snake_length = len(player_list)
        player = player_list[0]
        x, y = canvas.coords(player)
        if direction == "right":
            x += SIZE
        elif direction == "left":
            x -= SIZE
        elif direction == "up":
            y -= SIZE
        elif direction == "down":
            y += SIZE

        canvas.moveto(player, x, y)
        snake_path.insert(0, (x, y))

        for i in range(1, snake_length):
            canvas.moveto(player_list[i], snake_path[i - 1][0], snake_path[i - 1][1])

        time.sleep(DELAY)
        collision = collision_check(canvas, player)
        if collision:
            new_snake_block = create_block(canvas, goal_position)
            player_list.append(new_snake_block)
            canvas.delete(goal)
            goal, goal_position = create_goal(canvas)

        direction = choose_direction(canvas, direction)
        if direction is None:
            break

    end_game(canvas, player_list)


def choose_direction(canvas, direction):
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


def collision_check(canvas, player):
    player_coords = canvas.coords(player)
    overlapping_objects = canvas.find_overlapping(*player_coords)
    return len(overlapping_objects) > 1


def end_game(canvas, player_list):
    end_screen(canvas)
    print("Game Over")


def create_player(canvas):
    player = []
    block = create_block(canvas, [0, 0, SIZE, SIZE])
    player.append(block)
    return player


def create_block(canvas, coordinates):
    block = canvas.create_rectangle(*coordinates)
    return block


def create_goal(canvas):
    top_x = random.randint(0, (CANVAS_WIDTH - SIZE) // SIZE) * SIZE
    top_y = random.randint(0, (CANVAS_HEIGHT - SIZE) // SIZE) * SIZE
    goal_position = [top_x, top_y, top_x + SIZE, top_y + SIZE]
    return canvas.create_rectangle(*goal_position, color="orange"), goal_position


def end_screen(canvas):
    clear_canvas(canvas)
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, color="brown")
    canvas.create_text(
        CANVAS_WIDTH / 2,
        CANVAS_HEIGHT / 3,
        text="Game Over",
        fill="white",
        font=("Helvetica", 24, "bold"),
    )
    canvas.create_text(
        CANVAS_WIDTH / 2,
        CANVAS_HEIGHT / 2,
        text="Press Enter to play again",
        fill="white",
        font=("Helvetica", 18),
    )

    start_game(canvas)
    main()


if __name__ == "__main__":
    main()
