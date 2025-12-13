from itertools import groupby

from .part_1 import HomeworkProblem


def read_homework_from_columns_and_within_digit_columns(
    input: list[str],
) -> list[HomeworkProblem]:
    """Read values from digits within each column."""
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

    homework_problems = [
        HomeworkProblem.from_string_values(*values, operator)
        for values, operator in zip(
            operands,
            operators,
            strict=True,
        )
    ]

    return homework_problems
