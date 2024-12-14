from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import run

def part_1(input_path:str=get_default_input_path(__file__)):
    print(part_1_solve(input_path))

def part_1_solve(input_path:str) -> int:
    input_data = parse_input(input_path)
    return run(input_data, 25)
