def check_letters_order(input_text: str) -> bool:
    for i in range(len(input_text) // 2):
        if ord(input_text[i]) > ord(input_text[i + 1]):
            return False
    return True


def is_polyndrom(input_text: str) -> bool:
    index_end = len(input_text) - 1
    for i in range(len(input_text) // 2):
        if input_text[i] != input_text[index_end - i]:
            return False
    return True


def is_sorted_polyndrom(input_text: str) -> bool:
    if is_polyndrom(input_text) and check_letters_order(input_text):
        return True
    return False


if __name__ == '__main__':
    print(is_sorted_polyndrom("abcddcba"))
