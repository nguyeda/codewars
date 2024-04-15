def solution(number: int) -> int:
    fizz = set(range(3, number, 3))
    buzz = set(range(5, number, 5))
    return sum(fizz.union(buzz))
