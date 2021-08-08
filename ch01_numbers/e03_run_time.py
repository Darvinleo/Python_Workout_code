"""Solution to chapter 1, exercise 3: run_timing"""
from decimal import Decimal


def run_timing():
    """ Asks the user repeatedly for numeric input.
        Prints the average time and number of runs.
        Exits on pressing "Enter"
    """
    time_log = []
    while True:
        one_run = input("Enter your time for this 10 km: ")
        if not one_run:
            break
        try:
            time_log.append(float(one_run))
        except ValueError:
            print(
                "Hey, you enter something strange, "
                "please enter a valid number")
    avg_time = sum(time_log) / len(time_log)
    return f"Your average time is about: {avg_time:.1f}   " \
           f"over {len(time_log)} runs"


def digit_concats(a, b, c):
    """This is beyond the exercise task.
        :param a: float
        :param b: int
        :param c: int
        :return: float (b digits before a).count(c digits after)
    """
    a_str = str(a)
    p = a_str.index(".")
    return a_str[p - b:p] + a_str[p:p + c + 1]


def decimal_sum(*args):
    """Function takes strings of float and return their sum"""
    res = 0
    for numb in args:
        try:
            res += Decimal(str(numb))
        except:
            print(f"Argument [ {numb}  ]  is skipped... not a float")
    return res


print(run_timing())
# print(digit_concats(12345.67890, 3, 3))  # ==> return 345.678
# print(decimal_sum("3.14", 3.16, 0.5, "fsdf"))
