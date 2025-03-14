from cell import Cell
import time
import random

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._seed = seed

        if self._seed is not None:
            random.seed(self._seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_cols):
            columns = []
            for j in range(self._num_rows):
                columns.append(Cell(self._win))
            self._cells.append(columns)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_walls_r(self, i, j):
        print(f"Breaking walls at cell ({i}, {j})")
        self._cells[i][j].visited = True

        while True:
            routes = []
            if (i + 1) < self._num_cols and not self._cells[i + 1][j].visited:
                routes.append((i + 1, j))
            if (j + 1) < self._num_rows and not self._cells[i][j + 1].visited:
                routes.append((i, j + 1))
            if i > 0 and not self._cells[i - 1][j].visited:
                routes.append((i - 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                routes.append((i, j - 1))
            if not routes:
                self._draw_cell(i, j)
                return
            
            route_index = random.randrange(len(routes))
            next_i, next_j = routes[route_index]
            
            if next_i == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][j].has_left_wall = False
            if next_j == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][next_j].has_top_wall = False
            if next_i == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][j].has_right_wall = False
            if next_j == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][next_j].has_bottom_wall = False
            
            self._break_walls_r(next_i, next_j)
