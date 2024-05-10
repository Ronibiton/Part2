import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr


def get_numbers_from_user() -> []:
    numbers = []
    num = 0
    while num != -1:
        try:
            num = float(input("enter a number >>> "))
            if num == -1:
                break
            numbers.append(num)
        except:
            print("not a valid input, try again")
    return numbers


def get_avg(numbers: []) -> int:
    avg = 0
    for num in numbers:
        avg = avg + num
    return avg / len(numbers)


def get_amount_positive_numbers(numbers: []) -> int:
    count = 0
    for num in numbers:
        if num > 0:
            count = count + 1
    return count


def sort_numbers(numbers: []) -> []:
    return sorted(numbers)


def build_graph(numbers: []) -> None:
    length_numbers = []
    for i in range(1, len(numbers) + 1):
        length_numbers.append(i)
    x = np.array(length_numbers)
    y = np.array(numbers)
    plt.scatter(x, y)
    plt.show()


def pearson(numbers: []):
    index = []
    for i in range(1, len(numbers) + 1):
        index.append(i)
    pearson_correlation, _ = pearsonr(index, numbers)
    return pearson_correlation


def the_mathematical_operations():
    numbers = get_numbers_from_user()
    print(f"the average is: {get_avg(numbers)}")
    print(f"the input numbers contain {get_amount_positive_numbers(numbers)} positive number/s")
    print(f"the numbers by sort >>> {sort_numbers(numbers)}")
    print(f"pearson correlation is: {pearson(numbers)}")
    build_graph(numbers)


if __name__ == '__main__':
    the_mathematical_operations()
