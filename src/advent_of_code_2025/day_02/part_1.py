from functools import partial

from advent_of_code_2025.helpers import load_input


def read_and_split_input(file: str) -> list[tuple[str, str]]:
    """Read input and return as list of tuples [(a, b), (c, d),..]."""

    raw_input = load_input(file)

    split_inputs = [x.split("-") for x in raw_input[0].split(",")]

    return [(x[0], x[1]) for x in split_inputs]


def sum_invalid_ids(input: list[tuple[str, str]]) -> int:
    """Sum invalid ids in all ranges."""

    invalid_ids: list[str] = []

    for invalid_range in input:
        invalid_ids.extend(
            find_invalid_ids_in_range(lower=invalid_range[0], upper=invalid_range[1])
        )

    return sum([int(x) for x in invalid_ids])


def find_invalid_ids_in_range(lower: str, upper: str) -> list[str]:
    """Find all invalid ids within range."""

    invalid_ids: list[str] = []

    lower_limit_odd_number_digits = len(lower) % 2
    upper_limit_odd_number_digits = len(upper) % 2

    # numbers in the range have same odd number of digits
    if len(lower) == len(upper) and lower_limit_odd_number_digits == 1:
        return invalid_ids

    if lower_limit_odd_number_digits:
        # For odd number of digits in the lower limit the starting
        # value for the repeating digits is "1" followed by
        # n_repeated_digits - 1 "0"s
        n_repeated_digits = int((len(lower) + 1) / 2)
        start_repeated_digit = int(10 ** (n_repeated_digits - 1))
    else:
        # For even number of digits in the lower limit the starting
        # value for the repeating digits is the first half of the limit
        n_repeated_digits = int(len(lower) / 2)
        start_repeated_digit = int(lower[:n_repeated_digits])

    if upper_limit_odd_number_digits:
        # For odd number of digits in the upper limit
        end_repeated_digit = int("9" * int((len(upper) - 1) / 2))
    else:
        end_repeated_digit = int(upper[:n_repeated_digits])

    def repeated_digits_in_range(digits: int, lower: str, upper: str) -> bool:
        return int(lower) <= int(digits) <= int(upper)

    invalid_ids_in_range = list(
        filter(
            partial(repeated_digits_in_range, lower=lower, upper=upper),
            [
                2 * str(digits_to_repeat)
                for digits_to_repeat in range(
                    start_repeated_digit, end_repeated_digit + 1
                )
            ],
        )
    )

    invalid_ids.extend(invalid_ids_in_range)

    return invalid_ids
