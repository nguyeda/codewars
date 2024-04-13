from .main import continued_fraction


def test_basic():
    assert continued_fraction(311, 144) == [2, 6, 3, 1, 5]
    assert continued_fraction(761, 327) == [2, 3, 17, 1, 5]
    assert continued_fraction(1721, 9) == [191, 4, 2]


def test_div():
    assert continued_fraction(1089, 9) == [121]
    assert continued_fraction(11011, 13) == [847]
    assert continued_fraction(1173, 17) == [69]


def test_zero():
    assert continued_fraction(0, 15) == []
