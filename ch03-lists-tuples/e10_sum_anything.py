"""Solution to chapter 3, exercise 10: mysum"""


def mysum(*items):
    """
        Sum the passed arguments, which should be of the same type.
        The arguments should handle the + operator.
        If passed no arguments, then return an empty tuple.
    """
    if not items:
        return items
    out = items[0]
    for x in items[1:]:
        out += x
    return out


def mysum_bigger_then(wall, *items):
    """
    function takes a first argument that indicates the threshold for including
    an argument in the sum.
    """
    if not items:
        return items
    grt_lst = [item for item in items if item > wall]
    res = grt_lst[0]
    for x in grt_lst[1:]:
        res += x
    return res


def sum_numeric(*args):
    """
    Function takes any number of arguments. If the argument is or
    can be turned into an integer, then it's added to the total.
    """
    res = 0
    for x in args:
        try:
            res += int(x)
        except (ValueError, TypeError):
            pass
    return res


a = {'a': 1, 'b': 2, 'c': 3}
b = {'d': 1, 'e': 2, 'c': 5}
c = {'g': 2, 'y': 10, 'x': 12, 'c': 10}


def merge_dicts(*args):
    """
        function takes dicts and returns a single dict that combines
        all of the keys and values. If a key appears in more than one argument, the
        value should be a list containing all of the values from the arguments.
    """
    x = {k: [d.get(k) for d in list(args) if d.get(k)]
         for k in set().union(*list(args))}
    return {k: v[0] if len(v) == 1 else v for k, v in x.items()}


print(sum_numeric(1, '2', 3, '4', 5, 'sf', ['1', 1], (1, 2)))
print(mysum_bigger_then((1, 2), (2, 1), (1, 2), (2, 1)))
print(mysum([1, 2, 3], [4, 5, 6]))
print(merge_dicts(a, b, c))
