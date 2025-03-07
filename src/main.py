from graphics import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(2, 2, 50, 50)
    win.wait_for_close()

if __name__ == "__main__":
    main()