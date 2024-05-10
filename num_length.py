import math


def num_len(num: int) -> int:
    return math.ceil(math.log10(num))


if __name__ == '__main__':
    print(num_len(32132))
