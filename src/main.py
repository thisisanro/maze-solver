from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    size_x = 50
    size_y = 50
    num_rows = 8
    num_cols = 12
    maze = Maze(2, 2, num_rows, num_cols, size_x, size_y, win)

    win.wait_for_close()

if __name__ == "__main__":
    main()