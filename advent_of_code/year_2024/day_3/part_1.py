from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import mul_iter

def part_1(input_path:str=get_default_input_path(__file__)):
    print(part_1_solve(input_path))

def part_1_solve(input_path:str) -> int:
    input = parse_input(input_path)
    return sum(mul_iter(input))
