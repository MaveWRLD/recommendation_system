import pytest
from django.test import TestCase


def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    prev, current = 0, 1
    for _ in range(2, n + 1):
        prev, current = current, prev + current
    return current


@pytest.mark.parametrize(
    "n, expected", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (10, 55)]
)
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


# Create your tests here.
