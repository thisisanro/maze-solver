from graphics import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    
    cell = Cell(win)
    cell.draw(2, 2, 50, 50)

    cell2 = Cell(win)
    cell2.draw(51, 2, 101, 50)

    cell.draw_move(cell2)

    win.wait_for_close()

if __name__ == "__main__":
    main()