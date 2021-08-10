from random import randint


def nonsense(n):
    """
    Beyond exercise;  Take a text file, creating (and printing) a nonsensical
    sentence from the nth word on each of the first 10 lines,
    where n is the line number.
    """
    with open('somefile.txt', 'r') as Nonsense_file:
        head = [next(Nonsense_file) for x in range(n)]
    return " ".join([line.split()[randint(0, len(line.split()) - 1)]
                     for line in head])


def transpose(lst):
    """
        function that transposes a list of strings, in which each string
        contains multiple words separated by whitespace
        if you'll pass the list ['abc 1', 'def 2']
        to the function, it will return ['abc def', '1 2']
    """
    return [" ".join(x) for x in zip(*list(x.split() for x in lst))]


print(nonsense(5))
print(transpose(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))
