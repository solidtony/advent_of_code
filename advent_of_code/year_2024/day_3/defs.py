from pathlib import Path
import re
from typing import Generator


def parse_input(input_path:Path) -> str:
    input = ''
    for line in open(input_path, 'r'):
        input += line
    return input

# Part 1
def mul_iter(expression:str) -> Generator[int, None, None]:
    pattern = "(mul\(([0-9]{1,3}),([0-9]{1,3})\))"
    for match in re.finditer(pattern, expression):
        yield int(match.groups()[1]) * int(match.groups()[2])

# Part 2
def between_do_dont_mul_iter(expression:str) -> Generator[int, None, None]:
    pattern = "(?<=do\(\))[\S\s]*?(?=don't\(\))"
    value = "do()" + expression + "don't()"
    for match in re.finditer(pattern, value):
        for result in mul_iter(match.group()):
            yield result
