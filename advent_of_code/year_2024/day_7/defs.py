from itertools import product
from pathlib import Path
from typing import Callable
from typing import List
from typing import Tuple


def parse_input(input_path:Path) -> List[Tuple[int, List[int]]]:
    data = []
    for line in open(input_path, 'r'):
        result, operands = line.strip().split(':')
        result = int(result)
        operands = [int(operand) for operand in operands.strip().split()]
        data.append((result, operands))
    return data

def add(l:int, r:int) -> int:
    return l+r

def multiply(l:int, r:int) -> int:
    return l*r

def concatenation(l:int, r:int) -> int:
    mul = 10
    while(rh > mul):
        mul *= 10
    return lh*mul + rh

OPERATION_LIST = [add, multiply]
PART2_OPERATION_LIST = OPERATION_LIST + [concatenation]

def operator_combinations(operands:List[int], operation_list:List[Callable]=OPERATION_LIST) -> List[List[Callable]]:
    operation_combinations = product(operation_list, repeat=len(operands)-1)
    return [list(ops) for ops in operation_combinations]

def calc_result(operators:List[Callable], operands:List[int]) -> int:
    result = operators[0](operands[0], operands[1])
    operand_index = 2
    for operator in operators[1::]:
        result = operator(result, operands[operand_index])
        operand_index += 1
    return result

def is_valid(result:int, operands:List[int], operation_list:List[Callable]=OPERATION_LIST) -> bool:
    op_combs = operator_combinations(operands, operation_list)
    for operator in op_combs:
        res = calc_result(operator, operands)
        if result == res:
            return True
    return False
