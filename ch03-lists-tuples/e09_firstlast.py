"""Solution to chapter 3, exercise 9: firstlast"""


def firstlast(sequence):
    """
    takes a sequence (string, list, or tuple) and returns the first and
    last elements of that sequence, in a two-element sequence of the same type.
    """
    return sequence[:1] + sequence[-1:]


def even_odd_sums(lst):
    """
    takes a list or tuple of numbers. Return a two-element list,
    containing (respectively) the sum of the even-indexed numbers
    and the sum of theodd-indexed numbers.
    """
    return [sum(lst[::2]), sum(lst[1::2])]


def plus_minus(lst):
    """
    Write a function that takes a list or tuple of numbers.
    Return the result of alternately adding and subtracting numbers
    from each other. So calling the function as
    plus_minus([10, 20, 30, 40, 50, 60]), you’ll get back the result of
    10+20-30+40-50+60, or 50.
    """
    return lst[0] + sum(lst[1::2]) - sum(lst[2::2])


def myzip(x, y):
    """
    partly emulates the built-in zip function, taking any number of
    iterables and returning a list of tuples.
    """
    return [(x[i], y[i]) for i in range(len(min(x, y, key=len)))]


print(even_odd_sums([10, 20, 25, 35]))
print(plus_minus([10, 20, 30, 40, 50, 60]))
print(myzip([10, 20, 30], 'ab'))
