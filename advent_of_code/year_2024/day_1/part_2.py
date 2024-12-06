from advent_of_code.utils import get_default_input_path

from .defs import parse_input

def part_2(input_path:str=get_default_input_path(__file__)):
    print(part_2_solve(input_path))

def part_2_solve(input_path:str) -> int:
    left_list, right_list = parse_input(input_path)
    similarity_score = sum([l_val*right_list.count(l_val) for l_val in left_list])
    return similarity_score
