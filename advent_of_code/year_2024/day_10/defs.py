from pathlib import Path

from typing import Generator
from typing import List
from typing import Set
from typing import Tuple

def parse_input(input_path:Path) -> List[List[int]]:
    data = []
    for line in open(input_path, 'r'):
        data.append([int(val) for val in line.strip()])
    return data

def iter_trail_heads(table:List[List[int]]) -> Generator[Tuple[int, int], None, None]:
    for row in range(len(table)):
        for col, value in enumerate(table[row]):
            if value == 0:
                yield row, col

def find_paths(table:List[List[int]], row:int, col:int) -> List[Tuple[int, int]]:
    if table[row][col] == 9:
        return [(row, col)]
    n_rows = len(table)
    n_cols = len(table[0])
    cur_val = table[row][col]
    found = []
    if row > 0 and table[row-1][col] - cur_val == 1:
        found += find_paths(table, row-1, col)
    if row < n_rows-1 and table[row+1][col] - cur_val == 1:
        found += find_paths(table, row+1, col)
    if col > 0 and table[row][col-1] - cur_val == 1:
        found += find_paths(table, row, col-1)
    if col < n_cols-1 and table[row][col+1] - cur_val == 1:
        found += find_paths(table, row, col+1)

    return found
