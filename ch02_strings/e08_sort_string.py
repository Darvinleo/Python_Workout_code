"""
    Solution to chapter 2, exercise 8: sort_string
    beyond the exercice:
    - Given the string “Tom Dick Harry,” break it into individual words,
     and then sort those words alphabetically. Once they’re sorted, print
     them with commas (,) between the names.
    - Which is the last word, alphabetically, in a text file?
    - Which is the longest word in a text file?
"""


def strsort(a_string):
    """
        Takes a string as input,
        returns a string with its characters sorted.
    """
    spl_str = a_string.split()
    ll_word = len(max(spl_str, key=len))
    print(f"Last word alphabetically is: {sorted(spl_str)[-1]}")
    print(
        f"Longest words is: "
        f"{', '.join([word for word in spl_str if len(word) == ll_word])}")

    return ', '.join([''.join(sorted(word.lower())) for word in spl_str])


print(strsort('Tom Dicky Harry'))
