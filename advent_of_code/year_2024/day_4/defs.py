from pathlib import Path
import re
from typing import List
from typing import Generator


def parse_input(input_path:Path) -> List[str]:
    return [line.strip() for line in open(input_path, 'r')]


def get_col(table:List[str], row, col) -> str:
    return ''.join([row[col] for row in table])

def get_rd_diagonal(table:List[str], row, col) -> str:
    n_steps = min(len(table) - row, len(table[0]) - col)
    return ''.join([
        table[row+step][col+step]
        for step in range(0,n_steps)
    ])

def get_ru_diagonal(table:List[str], row, col) -> str:
    n_steps = min(row+1, len(table[0]) - col)
    return ''.join([
        table[row-step][col+step]
        for step in range(0,n_steps)
    ])

def iterate_combinations(table:List[str]) -> Generator[str, None, None]:
    n_rows = len(table)
    n_cols = len(table[0])
    for row in table:
        yield row
    for col in range(0, n_cols):
        yield get_col(table, 0, col)
    for combination in iterate_diagonals(table):
        yield combination

def iterate_diagonals(table:List[str]) -> Generator[str, None, None]:
    n_rows = len(table)
    n_cols = len(table[0])
    for row in range(0, n_rows):
        yield get_rd_diagonal(table, row, 0)
        yield get_ru_diagonal(table, row, 0)
    row_index = n_rows-1
    for col in range(1, n_cols):
        yield get_rd_diagonal(table, 0, col)
        yield get_ru_diagonal(table, row_index, col)

def find_all(table:List[str], word:str) -> int:
    re_word = word[::-1]
    count = 0
    for expression in iterate_combinations(table):
        count += len(re.findall(word, expression))
        count += len(re.findall(re_word, expression))
    return count
