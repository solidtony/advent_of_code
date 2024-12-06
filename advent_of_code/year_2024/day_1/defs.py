from pathlib import Path
from typing import List
from typing import Tuple


def parse_input(input_path:Path) -> Tuple[List[int]]:
    left_list = []
    right_list = []
    for line in open(input_path, 'r'):
        left, right = line.strip().split()
        left_list.append(int(left))
        right_list.append(int(right))
    return left_list, right_list
