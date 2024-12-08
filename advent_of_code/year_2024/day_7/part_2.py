from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import PART2_OPERATION_LIST
from .defs import is_valid

def part_2(input_path:str=get_default_input_path(__file__)):
    print(part_2_solve(input_path))

def part_2_solve(input_path:str) -> int:
    input_data = parse_input(input_path)
    print('running ...')
    list_is_valid = [
        result
        for result, operands in input_data
        if is_valid(result, operands, PART2_OPERATION_LIST)
    ]
    return sum(list_is_valid)
