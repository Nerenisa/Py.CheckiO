#!/usr/bin/env python3
# coding: utf-8


def checkio(numbers_array: tuple) -> list:
    return sorted(list(numbers_array), key=abs)

# or return sorted(list(numbers_array), key=lambda n: -n if n < 0 else n)
    



if __name__ == '__main__':
    print('Example:')
    print(list(checkio((-20, -5, 10, 15))))

    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")