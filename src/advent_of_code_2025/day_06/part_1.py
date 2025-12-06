import operator
from dataclasses import dataclass
from functools import reduce
from typing import Callable


@dataclass
class HomeworkProblem:
    inputs: list[int]
    operator: Callable

    @classmethod
    def from_raw_values(cls, *args: str) -> "HomeworkProblem":
        """Read values from tuple of strings."""
        list_args: list[str] = list(*args)
        operator_string = list_args[-1]
        if operator_string == "+":
            operator_ = operator.add
        elif operator_string == "*":
            operator_ = operator.mul
        else:
            raise ValueError(f"Unexpected operator string: {operator_string}")
        return HomeworkProblem(
            inputs=[int(arg) for arg in list_args[0:-1]], operator=operator_
        )

    def calculate(self) -> int:
        """Calculate the homework problem solution."""
        return reduce(self.operator, self.inputs)


def transform_input_from_rows_to_columns(input: list[str]) -> list[HomeworkProblem]:
    """Convert input to list of column HomeworkProblem objects."""
    input_lines_split = [[x for x in line.split(" ") if len(x) > 0] for line in input]

    homework_problems = [
        HomeworkProblem.from_raw_values(items)  # type: ignore[arg-type]
        for items in zip(*input_lines_split[0:-1], input_lines_split[-1], strict=True)
    ]

    return homework_problems


def sum_cephalopod_math_homework(problems: list[HomeworkProblem]) -> int:
    """Calculate all homework problem solutions and sum result."""

    result = 0
    for homwork_problem in problems:
        result += homwork_problem.calculate()

    return result
