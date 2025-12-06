POINTS_ON_DIAL = 100


def count_times_pointing_at_zero(input: list[str], start_position: int = 50) -> int:
    """Count number of times dial lands on zero."""

    count = 0
    position = start_position

    for rotation_command in input:
        direction = rotation_command[0]
        rotation_size = int(rotation_command[1:])

        direciton_sign = 1 if direction == "R" else -1

        new_position, zero_passes = update_position_and_count_zero_passes(
            start_position=position, rotation=rotation_size * direciton_sign
        )

        count += zero_passes
        position = new_position

        # increment if the dial lands on zero, only if there was some rotation
        if (position == 0) & (rotation_size > 0):
            count += 1

    return count


def update_position_and_count_zero_passes(
    start_position: int, rotation: int
) -> tuple[int, int]:
    """Update dial position and count the number of times zero is passed.

    Do not count if the dial ends on the 0 position.

    """
    count = 0

    end_position = (start_position + rotation) % POINTS_ON_DIAL

    complete_rotations = abs(rotation) // POINTS_ON_DIAL

    # if starting and ending on zero do not count as another pass
    if start_position == 0 and end_position == 0 and complete_rotations > 0:
        complete_rotations -= 1

    count += complete_rotations

    if rotation < 0:
        if start_position > 0 and end_position > start_position:
            count += 1

    else:
        if end_position > 0 and end_position < start_position:
            count += 1

    return end_position, count
