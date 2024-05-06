import matplotlib.pyplot as plt
import numpy as np


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


def sort_num(numbers: []) -> []:
    sorted_numbers = []
    sorted_numbers.append(numbers[0])
    for i in range(1, len(numbers)):
        for j in range(len(sorted_numbers)):
            if numbers[i] <= sorted_numbers[j]:
                sorted_numbers.insert(j, numbers[i])
                break
            elif numbers[i] > sorted_numbers[len(sorted_numbers) - 1]:
                sorted_numbers.append(numbers[i])
    return sorted_numbers

###לא בטוחה אם נכון - אם זאת הכוונה
def build_graph(numbers : [])->None:
    length_numbers = []
    for i in range(1, len(numbers)+1):
        length_numbers.append(i)
    x = np.array(length_numbers)
    y = np.array(numbers)
    plt.scatter(x, y)
    plt.show()

if __name__ == '__main__':
    # print(get_numbers_from_user())
    # print(get_avg(get_numbers_from_user()))
    # print(get_amount_positive_numbers(get_numbers_from_user()))
    #print(sort_numbers([2, 6, 8, 4, 5, 1, -2, -7]))
    #print(sort_num([2, 6, 8, 4, 5, 1, -8, 1, -2, -7]))
    build_graph([2,4,3,6,8])

