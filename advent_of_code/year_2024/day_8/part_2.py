from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import Table

def part_2(input_path:str=get_default_input_path(__file__)):
    print(part_2_solve(input_path))

def part_2_solve(input_path:str) -> int:
    input_data = parse_input(input_path)
    table = Table(input_data)

    for _ in range(0, 2):
        table.populate_antinodes()
        table.fill_table_with_antinodes()
    table.display()
    n_antinodes = table.n_antinodes
    return n_antinodes
