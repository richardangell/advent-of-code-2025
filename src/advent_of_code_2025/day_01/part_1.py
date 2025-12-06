import operator


def count_times_ending_at_zero(input: list[str]) -> int:
    """Count number of times dial lands on zero."""

    count = 0
    position = 50
    points = 100

    for rotation_command in input:
        direciton = operator.add if rotation_command[0] == "R" else operator.sub

        position = direciton(position, int(rotation_command[1:])) % points

        if position == 0:
            count += 1

    return count
