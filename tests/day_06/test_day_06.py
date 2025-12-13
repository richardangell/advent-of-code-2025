import pytest

from advent_of_code_2025.day_06.part_1 import (
    sum_cephalopod_math_homework,
    transform_input_from_rows_to_columns,
)
from advent_of_code_2025.day_06.part_2 import (
    sum_cephalopod_math_homework_by_columns,
)
from advent_of_code_2025.helpers import load_input


@pytest.mark.parametrize(
    ["input_file", "expected"],
    [("tests/day_06/case_1.txt", 4277556), ("tests/day_06/input_1.txt", 3261038365331)],
)
def test_part_1(input_file: str, expected: int) -> None:
    raw_input = load_input(input_file)

    homework_problems = transform_input_from_rows_to_columns(raw_input)

    actual = sum_cephalopod_math_homework(homework_problems)

    assert actual == expected


@pytest.mark.parametrize(
    ["input_file", "expected"],
    [("tests/day_06/case_1.txt", 3263827), ("tests/day_06/input_1.txt", 8342588849093)],
)
def test_part_2b(input_file: str, expected: int) -> None:
    input = load_input(input_file, remove_lines_breaks=True)

    actual = sum_cephalopod_math_homework_by_columns(input)

    assert actual == expected
