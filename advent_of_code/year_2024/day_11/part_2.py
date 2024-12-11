from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import iter_steps

def part_2(input_path:str=get_default_input_path(__file__)):
    print(part_2_solve(input_path))

n_stones = 0
def part_2_solve(input_path:str) -> int:
    input_data = parse_input(input_path)
    print('running: ...')
    index = 0
    wait_symbols = ['-','/','-','\\']
    for stones in iter_steps(input_data, 75):
        print(f'...{wait_symbols[index]}', end="\r")
        index = (index + 1) % 4
        n_stones = len(stones)
    return n_stones
