from functools import reduce
from itertools import groupby
from operator import add, mul


def sum_cephalopod_math_homework_by_columns(input: list[str]) -> int:
    operators = input[-1].split()

    # Split characters by row
    individual_characters_by_row = [list(line) for line in input[:-1]]

    # Transpose list of lists
    individual_characters_by_column = [
        list(x) for x in zip(*individual_characters_by_row, strict=True)
    ]

    # Join each column of characters
    concatenated_chracters_by_column = [
        "".join(column) for column in individual_characters_by_column
    ]

    # Pull out the items between space only items into lists
    operands = [
        list(element)
        for key, element in groupby(
            concatenated_chracters_by_column, lambda x: not x.isspace()
        )
        if key
    ]

    ops = {"*": mul, "+": add}
    total = 0
    for operator, current_operands in zip(operators, operands, strict=True):
        total += reduce(ops[operator], [int(x) for x in current_operands])
    return total
