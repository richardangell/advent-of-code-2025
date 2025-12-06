import pytest

from advent_of_code_2025.day_02.part_1 import (
    find_invalid_ids_in_range,
    read_and_split_input,
    sum_invalid_ids,
)


@pytest.mark.parametrize(
    ["input_file", "expected"],
    [
        ("tests/day_02/case_1.txt", 1227775554),
        ("tests/day_02/input_1.txt", 18700015741),
    ],
)
def test_part_1(input_file: str, expected: int) -> None:
    input = read_and_split_input(input_file)

    actual = sum_invalid_ids(input)

    assert actual == expected


@pytest.mark.parametrize(
    ["lower", "upper", "expected"],
    [
        ("11", "22", ["11", "22"]),
        ("95", "115", ["99"]),
        ("998", "1012", ["1010"]),
        ("1188511880", "1188511890", ["1188511885"]),
        ("222220", "222224", ["222222"]),
        ("1698522", "1698528", []),
        ("446443", "446449", ["446446"]),
        ("38593856", "38593862", ["38593859"]),
        ("565653", "565659", []),
        ("824824821", "824824827", []),
        ("2121212118", "2121212124", []),
        ("6948", "9419", [2 * str(x) for x in range(69, 94)]),
    ],
)
def test_find_invalid_ids_in_range(lower: str, upper: str, expected: list[str]) -> None:
    actual = find_invalid_ids_in_range(lower=lower, upper=upper)

    assert actual == expected
