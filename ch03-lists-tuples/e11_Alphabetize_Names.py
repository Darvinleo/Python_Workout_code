"""Solution to chapter 3, exercise 11: alphabetize_names"""

from operator import itemgetter

PEOPLE = [{'first': 'Reuven', 'last': 'Lerner',
           'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump',
           'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin',
           'email': 'president@kremvax.ru'}
          ]


def alphabetize_names(list_of_dicts):
    """
    Take a list of dicts describing people, each with first/last/email as keys.
    Return a new list of dicts, sorted first by last name and then by first name.
    If passed an empty list, then return an empty list.
    """
    return sorted(list_of_dicts, key=itemgetter('last', 'first'))


def sort_abs(list_of_numbers):
    """
    Take a sequence of positive and negative numbers, returns list
    sorted by absolute value.
    """
    return sorted(list_of_numbers, key=abs)


def sort_vowels_count(list_of_strings):
    """
    Take a list of strings, returns list sorted by how many vowels strings contain
    """
    return sorted(list_of_strings,
                  key=lambda x: len([v.lower() for v in x if v in 'aeiouy']))


def sort_sum_numb(list_of_numbers):
    """
    Take a list of lists, with each list containing zero or more numbers,
    returns list sorted by the sum of each inner list’s numbers.
    """
    return sorted(list_of_numbers, key=sum)


# print(alphabetize_names(PEOPLE))
# print(sort_abs([-1, -5, -2, 3, 1, 8]))
# print(sort_vowels_count(['aabb', 'aAbi']))
# print((sort_sum_numb([[1, 2, 3], [2, 3, 4, 5], [1, 2, 4, 5]])))
