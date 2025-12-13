from dataclasses import dataclass
from functools import reduce
from operator import add, mul
from typing import Callable

OPERATOR_MAPPING = {"*": mul, "+": add}


@dataclass
class HomeworkProblem:
    """Homework problem containing operator to apply to values."""

    inputs: list[int]
    operator: Callable

    @classmethod
    def from_string_values(cls, *args: str) -> "HomeworkProblem":
        """Read values from tuple of strings."""
        list_args: list[str] = list(*args)
        return HomeworkProblem(
            inputs=[int(arg) for arg in list_args[:-1]],
            operator=OPERATOR_MAPPING[list_args[-1]],
        )

    def calculate(self) -> int:
        """Apply the operator to all the inputs."""
        return reduce(self.operator, self.inputs)


def read_homework_from_columns(input: list[str]) -> list[HomeworkProblem]:
    """Read values down each column into a HomeworkProblem."""
    input_lines_split_by_whitespace = [line.split() for line in input]

    homework_problems = [
        HomeworkProblem.from_string_values(items)  # type: ignore[arg-type]
        for items in zip(
            *input_lines_split_by_whitespace[:-1],
            input_lines_split_by_whitespace[-1],
            strict=True,
        )
    ]

    return homework_problems


def sum_cephalopod_math_homework(problems: list[HomeworkProblem]) -> int:
    """Calculate all homework problem solutions and sum result."""

    result = 0
    for homwork_problem in problems:
        result += homwork_problem.calculate()

    return result
