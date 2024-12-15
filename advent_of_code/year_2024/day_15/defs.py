from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from enum import Enum
from typing import Tuple


class Table(list):
    pass

class BoxTable(Table):
    def __init__(self, n_rows:int, n_cols:int, boxes_pos=[]):
        pass

def parse_input(input_path:Path) -> Tuple[Table, str]:
    table = Table() 
    instructions = ''
    is_reading_table = True
    for line in open(input_path, 'r'):
        if line == '\n':
            is_reading_table = False
            continue
        if is_reading_table:
            row = [col for col in line.strip()]
            table.append(row)
        else:
            instructions += line.strip()
    return table, instructions

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
    UP = '^'
    RIGHT = '>'
    LEFT = '<'
    DOWN = 'v'

    @staticmethod
    def dir_offset(dir_e:DirEnum) -> Pos:
        return DIR_MAP[dir_e.value]

DIR_MAP = {
    DirEnum.UP.value :    Pos(-1,  0),
    DirEnum.RIGHT.value : Pos( 0,  1),
    DirEnum.LEFT.value :  Pos( 0, -1),
    DirEnum.DOWN.value :  Pos( 1,  0),
}

class Object:
    SYMBOL = ''

    def __init__(self, start_pos:Pos):
        self._pos = start_pos

    @property
    def symbol(self) -> str:
        return self.SYMBOL

    @property
    def pos(self) -> Pos:
        return self._pos

    def move(self, direction:DirEnum) -> Pos:
        self._pos = self.pos + DirEnum.dir_offset(direction)

    def __str__(self) -> str:
        return self.SYMBOL

    @classmethod
    def __class_name__(cls) -> str:
        return cls.__name__

    def __repr__(self) -> str:
        return f'{self.__class_name__()}({self._pos})'

class Robot(Object):
    SYMBOL = '@'

class Box(Object):
    SYMBOL = 'O'

class Wall(Object):
    SYMBOL = '#'

def run(table:Table, inst:str) -> int:
    pass
