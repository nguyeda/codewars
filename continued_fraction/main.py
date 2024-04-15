"""
In this kata, you will have to return the continued fractionwiki of a fraction.

For example, if the numerator is 311 and the denominator is 144, then you would have to return [2, 6, 3, 1, 5], because:

311 / 144 = 2 + 1/(6 + 1/(3 + 1/(1 + 1/5)))

If the numerator is 0, you should return [].
"""


def continued_fraction(nu: int, de: int) -> list[int]:
    def generator(n, d):
        while n > 0 and d > 0:
            q, r = divmod(n, d)
            n, d = d, r
            yield q

    return list(generator(nu, de))
