from pathlib import Path
from typing import Generator
from typing import List
from typing import Tuple


def parse_input(input_path:Path) -> List[str]:
    return [line.strip() for line in open(input_path, 'r')]


class Table:
    VISITED_SYMBOL = 'X'
    OBSTACLE_SYMBOL = '#'
    OUT_OF_BOUNDS_SYMBOL = 'E'
    OBSTRUCTION_SYMBOL = 'O'
    EMPTY_SPACE_SYMBOL = '.'

    def __init__(self, table:List[str]):
        self._n_rows = len(table)
        self._n_cols = len(table[0])
        self._data = ''.join(table)
        self._start_pos = self._find_starting_pos()
        self._guard = Guard(*self._start_pos)
        self._data = [char for char in self._data]

    @property
    def start_pos(self) -> Tuple[int, int]:
        return self._start_pos

    @property
    def n_rows(self) -> int:
        return self._n_rows

    @property
    def n_cols(self) -> int:
        return self._n_cols

    @property
    def size(self) -> int:
        return len(self._data)

    def count_visited(self) -> int:
        return self._data.count(self.VISITED_SYMBOL)

    def display(self):
        for row in range(0, self.n_rows):
            print(''.join(self._data[row*self.n_cols:(row+1)*self.n_cols]))

    def get_value(self, row:int, col:int) -> str:
        index = self._get_index(row, col)
        return self._data[index] if index is not None else self.OUT_OF_BOUNDS_SYMBOL

    def insert_obstruction(self, row:int, col:int):
        index = self._get_index(row, col)
        if index is not None:
            self._data[index] = self.OBSTRUCTION_SYMBOL

    def step_update(self) -> bool:
        if self._is_blocked():
            self._turn_if_blocked()
        else:
            self._move_guard_forward()
        cur_index = self._get_guards_index()
        return cur_index is not None

    def iterate_update(self) -> Generator[int, None, None]:
        step = 0
        while(self.step_update()):
            step += 1
            yield step
        return None

    def _move_guard_forward(self):
        cur_index = self._get_guards_index()
        self._data[cur_index] = self.VISITED_SYMBOL
        self._guard.move_forward()
        new_index = self._get_guards_index()
        if new_index is None:
            self._data[cur_index] = self.VISITED_SYMBOL
        else:
            self._data[new_index] = self._guard.symbol

    def _turn_if_blocked(self):
        if self._is_blocked():
            self._guard.turn_right()
            cur_index = self._get_guards_index()
            self._data[cur_index] = self._guard.symbol

    def _is_blocked(self) -> bool:
        next_symbol = self._get_next_symbol()
        return next_symbol in [self.OBSTACLE_SYMBOL, self.OBSTRUCTION_SYMBOL]

    def _get_guards_index(self) -> int | None:
        cur_row, cur_col = self._guard.pos
        return self._get_index(cur_row, cur_col)

    def _get_next_symbol(self) -> str:
        cur_row, cur_col = self._guard.pos
        dir_row, dir_col = self._guard.dir
        next_row, next_col = (cur_row+dir_row, cur_col+dir_col)
        return self.get_value(next_row, next_col)

    def _find_starting_pos(self) -> Tuple[int, int]:
        index = self._data.index('^')
        row = int(index/self.n_cols)
        col = index - row*self.n_cols
        return row, col
        
    def _get_index(self, row:int, col:int) -> int | None:
        if col < 0 or col > self.n_cols-1 or row < 0 or row > self.n_rows-1:
            return None
        return row*self.n_cols + col


class Guard:
    def __init__(self, start_row:int, start_col:int):
        self._direction = Direction()
        self._row = start_row
        self._col = start_col

    @property
    def pos(self) -> Tuple[int, int]:
        return self._row, self._col

    @property
    def dir(self) -> Tuple[int, int]:
        return self._direction.dir

    @property
    def symbol(self) -> str:
        return self._direction.symbol

    def turn_right(self):
        self._direction.turn_right()

    def move_forward(self):
        row_dir, col_dir = self._direction.dir
        self._row += row_dir
        self._col += col_dir


class Direction:
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    DIR_LIST = [UP, RIGHT, DOWN, LEFT]
    SYMBOL_LIST = ['^', '>', 'V', '<']

    @property
    def dir(self) -> Tuple[int, int]:
        return self.DIR_LIST[self._dir_index]

    @property
    def symbol(self) -> str:
        return self.SYMBOL_LIST[self._dir_index]

    def __init__(self):
        self._dir_index = 0

    def turn_right(self):
       self._dir_index = (self._dir_index+1) % 4

    def turn_left(self):
        self._dir_index = (self._dir_index-1) % 4


def iter_potential_obstruction_pos(input_data:List[str]) -> Generator[Tuple[int, int], None, None]:
    i_table = Table(input_data)
    s_row, s_col = i_table.start_pos
    for step in i_table.iterate_update():
        pass
    for row in range(0, i_table.n_rows):
        for col in range(0, i_table.n_cols):
            if i_table.get_value(row, col) == Table.VISITED_SYMBOL or (row == s_row and col == s_col):
                yield row, col
    return None

def list_potential_obstruction_pos(input_data:List[str]) -> List[Tuple[int,int]]:
    return [pos for pos in iter_potential_obstruction_pos(input_data)]

def determine_if_is_in_loop(table:Table) -> bool:
    for step in table.iterate_update():
        if step > table.size*5:
            return True
    return False

def run_check_for_in_loop(input_data:List[str], pos:Tuple[int, int]) -> bool:
    row, col = pos
    table = Table(input_data)
    table.insert_obstruction(row, col)
    return determine_if_is_in_loop(table)
