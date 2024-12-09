from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Generator
from typing import List
from typing import Set


def parse_input(input_path:Path) -> List[str]:
    return [line.strip() for line in open(input_path, 'r')]


class Table:
    OUT_OF_BOUNDS_SYMBOL = 'E'
    EMPTY_SPACE_SYMBOL = '.'
    ANTINODES_SYMBOL = '#'
    RES_ANTINODES_SYMBOL = '~'

    def __init__(self, table:List[str]):
        self._n_rows = len(table)
        self._n_cols = len(table[0])
        self._data = [char for char in ''.join(table)]
        self._antinodes = set()
        self._res_antinodes = set()

    @property
    def n_rows(self) -> int:
        return self._n_rows

    @property
    def n_cols(self) -> int:
        return self._n_cols

    @property
    def size(self) -> int:
        return len(self._data)

    @property
    def n_antinodes(self) -> int:
        return len(self._antinodes)

    @property
    def n_res_antinodes(self) -> int:
        return len(self._res_antinodes)

    @property
    def antinodes(self) -> Set[Pos]:
        return self._antinodes

    @property
    def res_antinodes(self) -> Set[Pos]:
        return self._res_antinodes

    def display(self):
        for row in range(0, self.n_rows):
            print(''.join(self._data[row*self.n_cols:(row+1)*self.n_cols]))

    def get_value(self, pos:Pos) -> str:
        index = self._get_index(pos)
        return self._data[index] if index is not None else self.OUT_OF_BOUNDS_SYMBOL

    def try_add_antinode(self, pos:Pos) -> bool:
        index = self._get_index(pos)
        if index is not None:
            self._antinodes.add(index)
            return True
        return False

    def try_add_res_antinode(self, pos:Pos) -> bool:
        index = self._get_index(pos)
        if index is not None:
            self._res_antinodes.add(index)
            return True
        return False

    def populate_antinodes(self) -> int:
        for index in range(0, len(self._data)):
            this_symbol = self._data[index]
            if this_symbol != self.EMPTY_SPACE_SYMBOL:
                this_pos = self._get_pos(index)
                for match_pos in self._iter_pos_matches(this_symbol):
                    if match_pos == this_pos:
                        continue
                    diff = match_pos - this_pos
                    antinode_pos = 2*diff + this_pos
                    self.try_add_antinode(antinode_pos)
        return self.n_antinodes

    def populate_res_antinodes(self) -> int:
        for index in range(0, len(self._data)):
            this_symbol = self._data[index]
            if this_symbol != self.EMPTY_SPACE_SYMBOL:
                this_pos = self._get_pos(index)
                for match_pos in self._iter_pos_matches(this_symbol):
                    if match_pos == this_pos:
                        continue
                    diff = match_pos - this_pos
                    multiplyer = 0
                    while(self.try_add_res_antinode(multiplyer*diff + this_pos)):
                        multiplyer += 1
        return self.n_res_antinodes

    def fill_table_with_antinodes(self):
        for antinode_index in self.antinodes:
            if self._data[antinode_index] == self.EMPTY_SPACE_SYMBOL:
                self._data[antinode_index] = self.ANTINODES_SYMBOL

    def fill_table_with_res_antinodes(self):
        for res_an_index in self.res_antinodes:
            if self._data[res_an_index] == self.EMPTY_SPACE_SYMBOL:
                self._data[res_an_index] = self.RES_ANTINODES_SYMBOL

    def _get_index(self, pos:Pos) -> int | None:
        if pos.col < 0 or pos.col > self.n_cols-1 or pos.row < 0 or pos.row > self.n_rows-1:
            return None
        return pos.row*self.n_cols + pos.col

    def _get_pos(self, index:int) -> Pos:
        row = int(index/self.n_cols)
        col = index - row*self.n_cols
        return Pos(row, col)

    def _iter_index_matches(self, symbol:str) -> Generator[int, None, None]:
        for index, val in enumerate(self._data):
            if val == symbol:
                yield index
        return None

    def _iter_pos_matches(self, symbol:str) -> Generator[Pos, None, None]:
        for index in self._iter_index_matches(symbol):
            yield self._get_pos(index)
        return None

@dataclass
class Pos:
    row:int
    col:int

    def __add__(self, other:Pos) -> Pos:
        return Pos(self.row + other.row, self.col + other.col)

    def __rmul__(self, scaler:int) -> Pos:
        return Pos(scaler*self.row, scaler*self.col)

    def __sub__(self, other:Pos) -> Pos:
        return Pos(self.row - other.row, self.col - other.col)
