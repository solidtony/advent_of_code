from typing import List

from advent_of_code.utils import get_default_input_path

from .defs import parse_input

def part_2(input_path:str=get_default_input_path(__file__)):
    print(part_2_solve(input_path))

def part_2_solve(input_path:str) -> int:
    input = parse_input(input_path)
    return count_x_mas(input)

def count_x_mas(table:List[str]) -> int:
    count = 0
    for row in range(1, len(table)-1):
        for col in range(1, len(table[0])-1):
            if table[row][col] == 'A':
                diags = ''.join([
                    table[row-1][col-1],
                    table[row+1][col-1],
                    table[row+1][col+1],
                    table[row-1][col+1],
                ])
                if diags in ['MMSS', 'SMMS', 'SSMM', 'MSSM']:
                    count += 1
    return count
