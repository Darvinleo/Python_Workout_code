"""Solution to chapter 1, exercise 2: mysum"""


def mysum(*numbers):
    """Accepts any number of numeric arguments as inputs.
Returns the sum of those numbers.
If invoked without any arguments, returns 0.
"""
    res = 0
    for number in numbers:
        try:
            number = int(number)
            res += number
        except ValueError:
            pass
    return res


print(mysum(*[10, 30, 25, *[10, 20]], 10, 'five', '5'))
