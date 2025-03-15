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
        self._reset_cells_visited()

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

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i + 1 == self._num_cols and j + 1 == self._num_rows:
            return True
        
        directions = [(1, 0, "right"), (0, 1, "down"), (-1, 0, "left"), (0, -1, "up")]
        for diri, dirj, dir in directions:
            new_i = i + diri
            new_j = j + dirj

            if (0 <= new_i < self._num_cols
                and 0 <= new_j < self._num_rows
                and not self._cells[new_i][new_j].visited):

                can_move = False
                if dir == "right" and not self._cells[i][j].has_right_wall:
                    can_move = True
                elif dir == "down" and not self._cells[i][j].has_bottom_wall:
                    can_move = True
                elif dir == "left" and not self._cells[i][j].has_left_wall:
                    can_move = True
                elif dir == "up" and not self._cells[i][j].has_top_wall:
                    can_move = True
                
                if can_move:
                    self._cells[i][j].draw_move(self._cells[new_i][new_j])
                    if self._solve_r(new_i, new_j):
                        return True
                    self._cells[i][j].draw_move(self._cells[new_i][new_j], True)

        return False
