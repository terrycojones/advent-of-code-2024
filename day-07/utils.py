import sys


def readInput():
    data = []
    for line in sys.stdin:
        result, *factors = map(int, line.replace(":", " ").split())
        data.append((result, tuple(factors)))

    return data


def check(result, factors, operators):
    assert len(factors) == len(operators) + 1
    value = factors[0]
    for factor, operator in zip(factors[1:], operators):
        value = operator(value, factor)
        if value > result:
            return False

    return value == result


def solve(perms):
    data = readInput()
    total = 0

    for result, factors in data:
        for operators in perms(len(factors) - 1):
            if check(result, factors, operators):
                total += result
                break

    print(total)
