from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import iter_trail_heads
from .defs import find_paths

def part_1(input_path:str=get_default_input_path(__file__)):
    print(part_1_solve(input_path))

def part_1_solve(input_path:str) -> int:
    input_data = parse_input(input_path)
    sum_score = 0
    for head_row, head_col in iter_trail_heads(input_data):
        paths = set()
        for path in find_paths(input_data, head_row, head_col):
            paths.add(path)
        sum_score += len(paths)
    return sum_score
