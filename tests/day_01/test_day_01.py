import pytest

from advent_of_code_2025.day_01.part_1 import count_times_pointing_at_zero
from advent_of_code_2025.helpers import load_input


@pytest.mark.parametrize(
    ["input_file", "expected"],
    [("tests/day_01/case_1.txt", 3), ("tests/day_01/input_1.txt", 1147)],
)
def test_part_1(input_file: str, expected: int) -> None:
    input = load_input(input_file)

    actual = count_times_pointing_at_zero(input)

    assert actual == expected
