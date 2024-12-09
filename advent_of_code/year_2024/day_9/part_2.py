from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import mem_map_to_disk_map
from .defs import compact_disk_map
from .defs import checksum_disk_map

def part_2(input_path:str=get_default_input_path(__file__)):
    print(part_2_solve(input_path))

def part_2_solve(input_path:str) -> int:
    input_data = parse_input(input_path)
    print('running ...')
    disk_map = mem_map_to_disk_map(input_data)
    co_disk_map = compact_disk_map(disk_map)
    return checksum_disk_map(co_disk_map)
