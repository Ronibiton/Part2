import math


def reverse_n_pi_digits(num: int):
    pi = str(math.pi)
    return pi[num::-1]


if __name__ == '__main__':
    print(reverse_n_pi_digits(4))
