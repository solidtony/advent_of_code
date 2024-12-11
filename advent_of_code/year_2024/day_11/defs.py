from pathlib import Path
from typing import Generator
from typing import List


def parse_input(input_path:Path) -> List[int]:
    return [int(element)
        for line in open(input_path, 'r')
        for element in line.strip().split()
    ]

def iter_steps(stones:List[int], n_steps:int) -> Generator[List[int], None, None]:
    new_stones = stones.copy()
    for step in range(n_steps):
        for index in range(len(new_stones)-1, -1, -1):
            stone = new_stones[index]
            stone_str = str(stone)
            if stone == 0:
                new_stones[index] = 1
            elif len(stone_str)%2 == 0:
                half_index = int(len(stone_str)/2)
                new_stones[index] = int(stone_str[half_index:])
                new_stones.insert(index, int(stone_str[0:half_index]))
            else:
                new_stones[index] = stone * 2024
        yield new_stones
    return None
