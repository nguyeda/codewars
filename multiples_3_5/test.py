import pytest
from .main import solution


@pytest.mark.parametrize(
    "n, expected",
    [
        (4, 3),
        (6, 8),
        (16, 60),
        (3, 0),
        (5, 3),
        (15, 45),
        (0, 0),
        (-1, 0),
        (10, 23),
        (20, 78),
        (200, 9168),
    ],
)
def test_case(n, expected):
    assert solution(n) == expected
