"""Helper functions for loading inputs."""


def load_input(
    file: str,
    remove_lines_breaks: bool = True,
) -> list[str]:
    """Load input with optional removal of line breaks."""
    with open(file) as f:
        lines = f.readlines()

    if remove_lines_breaks:
        lines = [x.replace("\n", "") for x in lines]

    return lines


def load_column_input(file: str, line_separator: str = " ") -> list[list[int]]:
    """Load input file with multiple columns.

    Column values are converted to ints.

    """
    lines = load_input(file)

    lines_split = [x.split(line_separator) for x in lines]

    columns = []

    for column_index in range(len(lines_split[0])):
        column = [int(x[column_index]) for x in lines_split]

        columns.append(column)

    return columns


def load_row_input(file: str, line_separator: str = " ") -> list[list[int]]:
    """Load input file with multiple rows.

    Row values are converted to ints.

    """
    lines = load_input(file)

    lines_split = [x.split(line_separator) for x in lines]

    lines_split_int = [[int(x) for x in line] for line in lines_split]

    return lines_split_int
