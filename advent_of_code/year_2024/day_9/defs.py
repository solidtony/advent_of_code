from pathlib import Path
from typing import List
from typing import Tuple


def parse_input(input_path:Path) -> str:
    mem_map = ''
    for line in open(input_path):
       mem_map += line.strip()
    return mem_map

FREE_SPACE_SYMBOL = '.'

def validate_mem_map(input_data:str):
    if not input_data.isdigit():
        msg = f'contains non-digit value: {input_data}'
        raise ValueError(msg)

def mem_map_to_disk_map(mem_map:str) -> List[str]:
    validate_mem_map(mem_map)
    files = mem_map[0::2]
    free_spaces = mem_map[1::2] + '0' # disk_space at end is assumed 0
    disk_map = []
    index = 0
    for n_file, n_free_space in zip(files, free_spaces):
        disk_map += int(n_file)*[str(index)]
        disk_map += int(n_free_space)*[FREE_SPACE_SYMBOL]
        index += 1
    return disk_map

def make_contiguous_disk_map(disk_map:List[str]) -> List[str]:
    co_disk_map = disk_map.copy()
    front_index = 0
    for back_index in range(len(co_disk_map)-1, -1, -1):
        if co_disk_map[back_index] != FREE_SPACE_SYMBOL:
            while(co_disk_map[front_index] != FREE_SPACE_SYMBOL):
                front_index += 1
            if front_index > back_index:
                break
            co_disk_map[back_index] = disk_map[front_index]
            co_disk_map[front_index] = disk_map[back_index]
    return co_disk_map

def compact_disk_map(disk_map:List[str]) -> List[str]:
    co_disk_map = disk_map.copy()
    for f_index, f_size in rev_iter_file_block(disk_map):
        for fs_index, fs_size in iter_free_space(co_disk_map):
            if fs_index + fs_size > len(co_disk_map):
                return co_disk_map
            if fs_index >= f_index:
                break
            if f_size <= fs_size:
                for offset in range(0, f_size):
                    co_disk_map[fs_index+offset] = disk_map[f_index+offset]
                    co_disk_map[f_index+offset] = disk_map[fs_index+offset]
                break
    return co_disk_map

def iter_free_space(disk_map:List[str]) -> Tuple[int,int]:
    index = 0
    last_index = len(disk_map) - 1
    while(index < last_index):
        block_size = 0
        if disk_map[index] == FREE_SPACE_SYMBOL:
            while(
                index + block_size < last_index
                and disk_map[index + block_size] == FREE_SPACE_SYMBOL
            ):
                block_size += 1
            yield index, block_size
        index += block_size + 1
    return None

def rev_iter_file_block(disk_map:List[str]) -> Tuple[int, int]:
    index = len(disk_map) - 1
    while(index > 0):
        block_size = 0
        cur_symbol = disk_map[index]
        if cur_symbol != FREE_SPACE_SYMBOL:
            while(
                index - block_size > -1
                and disk_map[index - block_size] == cur_symbol
            ):
                block_size += 1
            index -= block_size
            yield index+1, block_size
        else:
            index -= 1
    return None

def checksum_disk_map(disk_map:List[str]) -> int:
    sum = 0
    for index, value in enumerate(disk_map):
        if value == FREE_SPACE_SYMBOL:
            continue
        sum += index*int(value)
    return sum
