# it should return the continued fraction of de/nu in an array
def continued_fraction(nu: int, de: int) -> list[int]:
    def generator(n, d):
        while n > 0 and d > 0:
            q, r = divmod(n, d)
            n, d = d, r
            yield q

    return list(generator(nu, de))
