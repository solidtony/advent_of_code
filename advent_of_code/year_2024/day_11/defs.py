from pathlib import Path
from typing import Generator
from typing import Dict


def parse_input(input_path:Path) -> Dict[int, int]:
    stones = {}
    for line in open(input_path, 'r'):
        for stone in line.strip().split():
            stones[int(stone)] = 1 + stones.get(stone, 0)
    return stones

def run(stones:Dict[int, int], n_steps:int) -> int:
    for step in range(n_steps):
        print(f'running: {step+1}/{n_steps}', end='\r')
        items = [(stone, count) for stone, count in stones.items()]
        for stone, count in items:
            stone_str = str(stone)
            if stone == 0:
                remove_stones(stones, stone, count)
                add_stones(stones, 1, count)
            elif len(stone_str)%2 == 0:
                half_index = int(len(stone_str)/2)
                stone_1 = int(stone_str[0:half_index])
                stone_2 = int(stone_str[half_index:])
                remove_stones(stones, stone, count)
                add_stones(stones, stone_1, count)
                add_stones(stones, stone_2, count)
            else:
                new_stone = stone * 2024
                remove_stones(stones, stone, count)
                add_stones(stones, new_stone, count)
    print('', end='\n')
    return count_stones(stones)

def count_stones(stones:Dict[int, int]) -> int:
    total = 0
    for count in stones.values():
        total += count
    return total

def remove_stones(stones:Dict[int, int], stone:int, count:int):
    stones[stone] = stones.get(stone, 1) - count
    if stones[stone] < 1:
        del stones[stone]

def add_stones(stones:Dict[int, int], stone:int, count:int):
    stones[stone] = count + stones.get(stone, 0)
