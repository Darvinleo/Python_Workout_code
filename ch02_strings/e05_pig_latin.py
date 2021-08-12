"""Solution to chapter 2, exercise 5: pig_latin"""
import string


def pig_latina(word):
    """Translates a word into Pig Latin.
The "word" parameter is assumed to be an
English word, returned as a string.
"""
    # get punctuation from the end of the word
    w_end = punct_shifter(word)
    # get word without punctuation
    word = word[0:len(word) - len(punct_shifter(word))]
    # check contains word two same vowels
    uniq_vowels = len(set([x.lower() for x in word if x in 'aeiou']))
    if word.isdecimal():
        return word + w_end
    try:
        if word[0] in 'AaEeIiOoUu':
            return f"{word[0:1] + word[1:].lower()}way{w_end}"
        if word[0].istitle():
            return f"{word[1:].capitalize() + word[0:1].lower()}ay{w_end}"
        return f"{word[1:] + word[0:1]}ay{w_end}"
    except IndexError:
        return w_end


def punct_shifter(word):
    """
    This function handles punctuation
    If a word ends with punctuation, then that punctuation
    is shifted to the end of the translated word.
    """
    if word[-1] in string.punctuation + ' ':
        punct = []
        for char in reversed(word):
            if char not in string.punctuation + ' ':
                break
            punct.append(char)
        return ''.join(list(reversed(punct)))
    return ''

# print(pig_latina('Word'))
