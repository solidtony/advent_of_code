from pathlib import Path
from typing import List


def parse_input(input_path:Path) -> List[int]:
    input = []
    for line in open(input_path, 'r'):
        entry = [int(value) for value in line.strip().split(' ')]
        input.append(entry)
    return input


def get_sign(value:float) -> float:
    return 0 if value == 0 else value/abs(value)

def is_safe(report:List[int]) -> bool:
    dir = get_sign(report[1] - report[0])
    for first, second in zip(report[0:-1], report[1:]):
        offset = second - first
        offset_sq = offset*offset
        if (offset_sq > 9) or (offset_sq < 1) or (get_sign(offset) != dir):
            return False
    return True

def is_safe_with_dampener(report:List[int]) -> bool:
    for ignore_index in range(0, len(report)):
        if is_safe(report[:ignore_index] + report[ignore_index+1:]):
            return True
    return False
