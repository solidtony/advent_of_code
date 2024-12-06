from dataclasses import dataclass
from pathlib import Path
from typing import Dict
from typing import Generator
from typing import List
from typing import Set


@dataclass
class InputInfo:
    sort_rules:Dict[int, Set[int]]
    updates:List[List[int]]

def parse_input(input_path:Path) -> InputInfo:
    sort_rules = {}
    updates = []
    is_sort_data = True
    for line in open(input_path, 'r'):
        if line == '\n':
            is_sort_data = False
        elif is_sort_data:
            page, pred = [int(val) for val in line.split('|')]
            entry = sort_rules.get(page, set())
            entry.add(pred)
            sort_rules[page] = entry
        else:
            updates.append([int(pg) for pg in line.strip().split(',')])
    return InputInfo(sort_rules, updates)

def is_correct_order(input_info:InputInfo, update:List[int]) -> bool:
    for pg_index in range(1, len(update)):
        preceding_pgs = input_info.sort_rules.get(update[pg_index], set())
        for pre_pg in preceding_pgs:
            if pre_pg in update[:pg_index]:
                return False
    return True

def get_middle_value(update:List[int]):
    mid_index = int((len(update) - 1)/2)
    return update[mid_index]


# Part 1
def iterate_correct_middle(input_info:InputInfo) -> Generator[int, None, None]:
    for update in input_info.updates:
        if is_correct_order(input_info, update):
            yield get_middle_value(update)
    return


# Part 2
def iterate_incorrect_middle(input_info:InputInfo) -> Generator[int, None, None]:
    for update in input_info.updates:
        if not is_correct_order(input_info, update):
            ordered = ordered_correctly(input_info, update)
            yield get_middle_value(ordered)
    return

def ordered_correctly(input_info:InputInfo, update:List[int]) -> List[int]:
    ordered_update = update.copy()
    while(not is_correct_order(input_info, ordered_update)):
        for pg_index in range(1, len(ordered_update)):
            preceding_pgs = input_info.sort_rules.get(ordered_update[pg_index], set())
            for pre_pg in preceding_pgs:
                try:
                    found_index = ordered_update.index(pre_pg, 0, pg_index)
                    pg = ordered_update[pg_index]
                    ordered_update[pg_index] = ordered_update[found_index]
                    ordered_update[found_index] = pg
                except ValueError:
                    pass
    return ordered_update
