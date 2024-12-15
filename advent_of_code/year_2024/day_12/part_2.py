from advent_of_code.utils import get_default_input_path

from .defs_2 import parse_input
from .defs_2 import run

def part_2(input_path:str=get_default_input_path(__file__)):
    print(part_2_solve(input_path))

def part_2_solve(input_path:str) -> int:
    input_data = parse_input(input_path)
    return run(input_data)
