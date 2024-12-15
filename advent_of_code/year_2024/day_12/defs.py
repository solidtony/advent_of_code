from pathlib import Path
from typing import Callable
from typing import List
from typing import Tuple


def parse_input(input_path:Path) -> List[List[str]]:
    return [
        [ val for val in line.strip() ]
        for line in open(input_path, 'r')
    ]

def list_neighbors(table, row, col) -> List[Tuple[int, int]]:
    n_rows = len(table)
    n_cols = len(table[0])
    neighbors = []
    if row > 0:
        neighbors.append((row-1, col))
    if col > 0:
        neighbors.append((row, col-1))
    if row < n_rows - 1:
        neighbors.append((row+1, col))
    if col < n_cols - 1:
        neighbors.append((row, col+1))
    return neighbors

def count_edges(table, row, col, fill_value:str) -> int:
    n_edges = 4
    values = [fill_value, table[row][col]]
    for n_row, n_col in list_neighbors(table, row, col):
        if table[n_row][n_col] in values:
            n_edges -= 1
    return n_edges

def fill(table:List[List[str]], row:int, col:int, value:str, edge_count:Callable=count_edges) -> Tuple[int, int]:
    area = 0
    perimiter = 0
    if table[row][col] == value:
        area += 1
        fill_value = f'{table[row][col]}_f'
        perimiter += edge_count(table, row, col, fill_value)
        table[row][col] = fill_value
        for n_row, n_col in list_neighbors(table, row, col):
            n_area, n_per = fill(table, n_row, n_col, value)
            area += n_area
            perimiter += n_per
    return area, perimiter

def run_part_1(table:List[List[str]]) -> int:
    total = 0
    for row in range(0, len(table)):
        for col in range(0, len(table[0])):
            if table[row][col][-1] != 'f':
                area, per = fill(table, row, col, table[row][col])
                total += area*per
    return total
