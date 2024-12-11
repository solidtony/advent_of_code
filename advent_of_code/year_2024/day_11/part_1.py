from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import iter_steps

def part_1(input_path:str=get_default_input_path(__file__)):
    print(part_1_solve(input_path))

n_stones = 0
def part_1_solve(input_path:str) -> int:
    input_data = parse_input(input_path)
    for stones in iter_steps(input_data, 25):
        n_stones = len(stones)
    return n_stones
