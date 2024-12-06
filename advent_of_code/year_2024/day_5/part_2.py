from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import iterate_incorrect_middle

def part_2(input_path:str=get_default_input_path(__file__)):
    print(part_2_solve(input_path))

def part_2_solve(input_path:str) -> int:
    input_info = parse_input(input_path)
    return sum(iterate_incorrect_middle(input_info))
