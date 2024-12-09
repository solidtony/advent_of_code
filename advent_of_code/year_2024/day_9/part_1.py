from advent_of_code.utils import get_default_input_path

from .defs import parse_input
from .defs import mem_map_to_disk_map
from .defs import make_contiguous_disk_map
from .defs import checksum_disk_map

def part_1(input_path:str=get_default_input_path(__file__)):
    print(part_1_solve(input_path))

def part_1_solve(input_path:str) -> int:
    input_data = parse_input(input_path)
    disk_map = mem_map_to_disk_map(input_data)
    co_disk_map = make_contiguous_disk_map(disk_map)
    return checksum_disk_map(co_disk_map)
