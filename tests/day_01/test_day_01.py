import pytest

from advent_of_code_2025.day_01.part_1 import count_times_ending_at_zero
from advent_of_code_2025.day_01.part_2 import (
    count_times_pointing_at_zero,
    update_position_and_count_zero_passes,
)
from advent_of_code_2025.helpers import load_input


@pytest.mark.parametrize(
    ["input_file", "expected"],
    [("tests/day_01/case_1.txt", 3), ("tests/day_01/input_1.txt", 1147)],
)
def test_part_1(input_file: str, expected: int) -> None:
    input = load_input(input_file)

    actual = count_times_ending_at_zero(input)

    assert actual == expected


@pytest.mark.parametrize(
    ["input_file", "expected"],
    [("tests/day_01/case_1.txt", 6), ("tests/day_01/input_1.txt", 6789)],
)
def test_part_2(input_file: str, expected: int) -> None:
    input = load_input(input_file)

    actual = count_times_pointing_at_zero(input)

    assert actual == expected


@pytest.mark.parametrize(
    ["input", "start", "expected"],
    [
        pytest.param("L0", 0, (0, 0), id="L0-0"),
        pytest.param("L1", 0, (99, 0), id="L1-0"),
        pytest.param("L99", 0, (1, 0), id="L99-0"),
        pytest.param("L100", 0, (0, 0), id="L100-0"),
        pytest.param("L101", 0, (99, 1), id="L101-0"),
        pytest.param("L199", 0, (1, 1), id="L199-0"),
        pytest.param("L200", 0, (0, 1), id="L200-0"),
        pytest.param("L201", 0, (99, 2), id="L201-0"),
        pytest.param("L0", 20, (20, 0), id="L0-20"),
        pytest.param("L19", 20, (1, 0), id="L19-20"),
        pytest.param("L20", 20, (0, 0), id="L20-20"),
        pytest.param("L21", 20, (99, 1), id="L21-20"),
        pytest.param("L119", 20, (1, 1), id="L119-20"),
        pytest.param("L120", 20, (0, 1), id="L120-20"),
        pytest.param("L121", 20, (99, 2), id="L121-20"),
        pytest.param("R0", 0, (0, 0), id="R0-0"),
        pytest.param("R1", 0, (1, 0), id="R1-0"),
        pytest.param("R99", 0, (99, 0), id="R99-0"),
        pytest.param("R100", 0, (0, 0), id="R100-0"),
        pytest.param("R101", 0, (1, 1), id="R101-0"),
        pytest.param("R199", 0, (99, 1), id="R199-0"),
        pytest.param("R200", 0, (0, 1), id="R200-0"),
        pytest.param("R201", 0, (1, 2), id="R201-0"),
        pytest.param("R19", 80, (99, 0), id="R19-80"),
        pytest.param("R20", 80, (0, 0), id="R20-80"),
        pytest.param("R21", 80, (1, 1), id="R20-80"),
        pytest.param("R119", 80, (99, 1), id="R119-80"),
        pytest.param("R120", 80, (0, 1), id="R120-80"),
        pytest.param("R121", 80, (1, 2), id="R121-80"),
    ],
)
def test_update_position_and_count_zero_passes(
    input: str, start: int, expected: tuple[int, int]
) -> None:
    direction = input[0]
    rotation_size = int(input[1:])
    direciton_sign = 1 if direction == "R" else -1

    actual_position, actual_count = update_position_and_count_zero_passes(
        start_position=start, rotation=rotation_size * direciton_sign
    )

    assert actual_position == expected[0]
    assert actual_count == expected[1]
