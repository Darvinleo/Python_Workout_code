"""
    Solution to chapter 2, exercise 6: pl_sentence
    We need to import here module from previous exercise
"""
from e05_pig_latin import pig_latina as pigl


def pl_sentence():
    """
        Get a sentence from the user, containing
        lowercase, unpuncutated words. Return the
        sentence, translated into Pig Latin.
        [ My code can handle punctuation and word.istitle = True words ]
    """
    sentence = input("Please input your sentence to convert to pig latina: ")
    return " ".join([pigl(word) for word in sentence.split()])


print(pl_sentence())

