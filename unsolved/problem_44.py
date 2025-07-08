#!/usr/bin/env python3



def pentagon_number(n: int) -> int:
    return (n * ((3 * n) - 1)) // 2


def gen_pentagon_numbers(amount: int = 200) -> list[int]:
    return [pentagon_number(n) for n in range(amount)]


def penta_sum_and_diff(j: int, k: int) -> bool:
    pass


if __name__ == '__main__':
    pass