from graphics import Window
from maze import Maze


def main():
    num_rows = 10
    num_cols = 14
    screen_x = 800
    screen_y = 600
    win = Window(screen_x, screen_y)

    maze = Maze(50, 50, num_rows, num_cols, 50, 50, win, 23)

    win.wait_for_close()

if __name__ == "__main__":
    main()