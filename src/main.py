from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    size_x = 23
    size_y = 23
    num_rows = 10
    num_cols = 10
    maze = Maze(2, 2, num_rows, num_cols, size_x, size_y, win)

    win.wait_for_close()

if __name__ == "__main__":
    main()