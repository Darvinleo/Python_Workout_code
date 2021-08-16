"""Solution to chapter 3, exercise 13: tuple_records"""
from operator import itemgetter, attrgetter
from collections import namedtuple

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]


def format_sort_records_tuples(list_of_tuples):
    """
    This function expects to get a list of tuples, each representing a person.
    Each tuple contains 3 elements - first name, last name, distance to travel.
    (The first two are strings, and the third is a float.)
    We return a list of strings, sorted by last name and then first name.
    """
    output = []
    template = '{1:<10} {0:10} {2:>5.2f}'
    for person in sorted(list_of_tuples, key=itemgetter(1, 0)):
        output.append(template.format(*person))
    return output


def format_sort_records_namedtuples(list_of_tuples):
    """Reimplement using namedtuple objects"""
    output = []
    n_tup = namedtuple('dude', 'f_name l_name time')
    dudes = [n_tup(*person) for person in list_of_tuples]
    for dude in sorted(dudes, key=attrgetter('f_name', 'l_name')):
        output.append(
            f"{dude.l_name:10} {dude.f_name:<10} {dude.time:>5.2f}")
    return output


print('\n'.join(format_sort_records_tuples(PEOPLE)))
print('='*27)
print('\n'.join(format_sort_records_namedtuples(PEOPLE)))
