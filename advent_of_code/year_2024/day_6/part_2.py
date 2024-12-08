from multiprocessing import Pool

from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import list_potential_obstruction_pos
from .defs import run_check_for_in_loop

def part_2(input_path:str=get_default_input_path(__file__)):
    print(part_2_solve(input_path))

def part_2_solve(input_path:str) -> int:
    input_data = parse_input(input_path)
    print('running: ...')
    potential_pos = list_potential_obstruction_pos(input_data)

    args = [[input_data, pos] for pos in potential_pos]
    with Pool(10) as p:
        results = p.map(run, args)

    return results.count(True)

def run(args) -> bool:
    return run_check_for_in_loop(*args)
