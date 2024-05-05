import math


def find_factors(c: int):
    factors = []
    factors_numbers = []
    for i in range(0, int(math.sqrt(c)) + 1):
        for j in range(0, int(math.sqrt(c)) + 1):
            if math.pow(i, 2) + math.pow(j, 2) == c:
                if i not in factors_numbers:
                    sum_factors = j + i + math.sqrt(c)
                    if j < i:
                        factors.append([j, i, c, sum_factors])
                        factors_numbers.append(j)
    return factors


def collect_factors(sum: int):
    all_factors = []
    for i in range(0, int(sum * sum // 2)):
        factors_options = find_factors(i)
        for factors in factors_options:
            if factors[3] > sum:
                break
            if factors not in all_factors and factors[3] == sum:
                all_factors.append(factors)
    return all_factors


def pythagorean_triplet_by_sum() -> None:
    sum = 0
    try:
        sum = int(input("please enter a sum number(natural number) >>> "))
    except:
        print("not a valid input")
    valid_options_factors = collect_factors(sum)
    for factors in valid_options_factors:
        print(f"{str(factors[0])} < {str(factors[1])} < {str(int(math.sqrt(factors[2])))}")


if __name__ == '__main__':
    pythagorean_triplet_by_sum()
