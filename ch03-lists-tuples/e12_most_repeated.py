"""Solution to chapter 3, exercise 12: most_repeating_word"""

from collections import Counter
# import sort_vowels_count function from previous exercice
from e11_Alphabetize_Names import sort_vowels_count as sv_count

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example', 'elementari']


def most_repeating_letter_count(word):
    """
    Given a non-empty string, counts how many times each letter
    appears in the string, and returns an integer indicating how
    often the most common letter appears.
    """
    return Counter(word.lower()).most_common(1)[0][1]


def most_repeating_word(words):
    """
    Given a list of non-empty strings (words),
    returns the word containing at least one letter that repeats
    more often than any letter in any other word.
    Because sorting in Python is stable, if multiple words have
    the same count, then the first will be returned.
    """
    return max(words, key=most_repeating_letter_count)


def most_repeating_vowels(words):
    """
    This function returns the words with the greatest number of repeated vowels.
    """
    return ' '.join([x for x in WORDS if len(x) == len(sv_count(words)[-1])])


# print(most_repeating_letter_count('BeEez'))
# print(most_repeating_word(['Beef', 'Beer', 'Duck']))
print(most_repeating_vowels(WORDS))
