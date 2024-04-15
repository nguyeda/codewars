import pytest

from .main import find_it


@pytest.mark.parametrize(
    "input, expected",
    [
        ([7], 7),
        ([0], 0),
        ([1, 1, 2], 2),
        ([0, 1, 0, 1, 0], 0),
        ([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1], 4),
    ],
)
def test_it(input, expected):
    assert find_it(input) == expected
