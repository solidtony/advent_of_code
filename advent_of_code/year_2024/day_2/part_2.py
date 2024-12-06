from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import is_safe_with_dampener

def part_2(input_path:str=get_default_input_path(__file__)):
    print(part_2_solve(input_path))

def part_2_solve(input_path:str) -> int:
    input = parse_input(input_path)
    results = [is_safe_with_dampener(report) for report in input]
    return results.count(True)