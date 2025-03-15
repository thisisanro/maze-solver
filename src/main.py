from graphics import Window
from maze import Maze


def main():
    num_rows = 10
    num_cols = 14
    indent = 50
    screen_x = 1280
    screen_y = 720
    cell_size_x = (screen_x - 2 * indent) / num_cols
    cell_size_y = (screen_y - 2 * indent) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(indent, indent, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("Maze created")
    solvable = maze.solve()
    if solvable:
        print("Maze solved")
    else:
        print("Maze is not solvable")

    win.wait_for_close()

if __name__ == "__main__":
    main()