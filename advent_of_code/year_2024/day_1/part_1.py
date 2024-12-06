from advent_of_code.utils import get_default_input_path

from .defs import parse_input

def part_1(input_path:str=get_default_input_path(__file__)):
    print(part_1_solve(input_path))

def part_1_solve(input_path:str) -> int:
    left_list, right_list = parse_input(input_path)
    sum_diffs = sum([abs(l_val - r_val) for l_val, r_val in zip(sorted(left_list), sorted(right_list))])
    return sum_diffs
