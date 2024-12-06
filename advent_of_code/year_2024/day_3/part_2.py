from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import between_do_dont_mul_iter

def part_2(input_path:str=get_default_input_path(__file__)):
    print(part_2_solve(input_path))

def part_2_solve(input_path:str) -> int:
    input = parse_input(input_path)
    return sum(between_do_dont_mul_iter(input))
