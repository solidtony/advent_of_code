from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Any
from typing import List
from typing import Tuple

from .defs import list_neighbors
from .defs import parse_input

@dataclass
class Pos:
    row:int
    col:int

    def __add__(lh, rh:Pos) -> Pos:
        return Pos(lh.row + rh.row, lh.col + rh.col)

    def __sub__(lh, rh:Pos) -> Pos:
        return Pos(lh.row - rh.row, lh.col - rh.col)

    def __rmul__(self, coef) -> Pos:
        return Pos(coef*self.row, coef*self.col)

    def __eq__(lh, rh:Pos) -> bool:
        return lh.row == rh.row and lh.col == rh.col

    def __hash__(self) -> int:
        return hash((self.row, self.col))

class DirEnum(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class DirLooker:
    dir_pos_list = [
        Pos(-1, 0), # UP
        Pos(0, 1), # Right
        Pos(1, 0), # Down
        Pos(0, -1), # Left
    ]

    def __init__(self, start_dir=DirEnum.UP):
        self._index = start_dir.value

    def turn_right(self):
        self._index = self._get_index(1)

    def turn_left(self):
        self._index = self._get_index(-1)

    def turn_back(self):
        self._index = self._get_index(2)

    def forward_diff(self) -> Pos:
        return self._get_dir_diff(0)

    def right_diff(self) -> Pos:
        return self._get_dir_diff(1)

    def left_diff(self) -> Pos:
        return self._get_dir_diff(-1)

    def backward_diff(self) -> Pos:
        return self._get_dir_diff(2)

    def _get_dir_diff(self, i_diff:int) -> Pos:
        return self.dir_pos_list[self._get_index(i_diff)]

    def _get_index(self, i_diff:int) -> int:
        return (self._index + i_diff) % 4

def get_value(table:List[List[int]], pos:Pos, default=0) -> int:
    if pos.row < 0 or pos.row > len(table)-1 or pos.col < 0 or pos.col > len(table[0])-1:
        return default
    return table[pos.row][pos.col]

DEFAULT_EDGE_SYMBOL = '-'
DEFAULT_INNER_SYMBOL = '+'

def count_edges(table:List[List[int]], b_val:int=DEFAULT_EDGE_SYMBOL) -> int:
    visited = set()
    n_sides = 0
    for row in range(0, len(table)):
        for col in range(0, len(table[0])):
            start_pos = Pos(row, col)
            if (not start_pos in visited) and (table[row][col] == b_val):
                cur_pos = Pos(row, col)
                dir_looker = DirLooker()
                end_dir = DirLooker()
                if get_value(table, cur_pos + dir_looker.forward_diff()) == DEFAULT_INNER_SYMBOL:
                    if get_value(table, cur_pos + dir_looker.right_diff()) == DEFAULT_EDGE_SYMBOL:
                        n_sides += 1
                        end_dir = DirLooker(DirEnum.LEFT)
                    elif get_value(table, cur_pos + dir_looker.backward_diff()) == DEFAULT_EDGE_SYMBOL:
                        n_sides += 2
                        end_dir = DirLooker(DirEnum.UP)
                    dir_looker = DirLooker(DirEnum.DOWN)
                end_dir_diff = end_dir.forward_diff()
                while(True):
                    if get_value(table, cur_pos + dir_looker.right_diff()) == b_val:
                        n_sides += 1
                        dir_looker.turn_right()
                    elif get_value(table, cur_pos + dir_looker.forward_diff()) == b_val:
                        pass
                    elif get_value(table, cur_pos + dir_looker.left_diff()) == b_val:
                        n_sides += 1
                        dir_looker.turn_left()
                    elif get_value(table, cur_pos + dir_looker.backward_diff()) == b_val:
                        n_sides += 2
                        dir_looker.turn_back()
                    else:
                        n_sides += 4
                        visited.add(cur_pos)
                        break
                    visited.add(cur_pos)
                    cur_pos = cur_pos + dir_looker.forward_diff()
                    if start_pos == cur_pos:
                        if dir_looker.forward_diff() == end_dir_diff:
                            break
    return n_sides

def boarder(table:List[List[int]], value:str) -> List[List[int]]:
    # create table padded by 1 around entire table filled with zeros
    b_table = [[0 for _ in range(0, 2+len(table[0]))] for _ in range(0, 2+len(table))]
    # fill table with values
    for row in range(0, len(table)):
        for col in range(0, len(table[0])):
            if table[row][col] == value:
                b_table[row+1][col+1] = DEFAULT_INNER_SYMBOL
    for row in range(0, len(b_table)):
        for col in range(0, len(b_table[0])):
            if b_table[row][col] == DEFAULT_INNER_SYMBOL:
                neighbors = [
                    (row-1, col-1),
                    (row-1, col),
                    (row-1, col+1),
                    (row, col+1),
                    (row+1, col+1),
                    (row+1, col),
                    (row+1, col-1),
                    (row, col-1),
                ]
                for n_row, n_col in neighbors:
                    if b_table[n_row][n_col] != DEFAULT_INNER_SYMBOL:
                        b_table[n_row][n_col] = DEFAULT_EDGE_SYMBOL
    return b_table


def fill(table:List[List[str]], row:int, col:int, fill_value:Any, value:str=None) -> int:
    n_filled = 0
    if value == None:
        value = table[row][col]
    if table[row][col] == value:
        table[row][col] = fill_value
        n_filled += 1
        for n_row, n_col in list_neighbors(table, row, col):
            n_filled += fill(table, n_row, n_col, fill_value, value)
    return n_filled

def display_table(table:List[List[str]]):
    for row in table:
        print(''.join([str(col) for col in row]))


def run(table:List[List[str]]) -> int:
    total = 0
    count = 1
    visited = set()
    for row in range(0, len(table)):
        for col in range(0, len(table[0])):
            if not table[row][col] in visited:
                value = table[row][col]
                area = fill(table, row, col, count)
                boarder_table = boarder(table,count)
                n_sides = count_edges(boarder_table)
                total += area*n_sides
                print(f'value: {value}; area: {area}; n_sides: {n_sides}; cost: {area*n_sides}')
                visited.add(count)
                count += 1
    return total
