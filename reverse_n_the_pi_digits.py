import mpmath
from mpmath import mp


def reverse_n_pi_digits(num: int):
    mp.dps = num + 1
    pi = str(mpmath.pi)
    return pi[num::-1]


if __name__ == '__main__':
    print(reverse_n_pi_digits(101))
