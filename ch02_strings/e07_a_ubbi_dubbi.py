def ubbi_dubbi(word):
    """
    This function takes a single word (string) as an argument.
    It returns a string, the word’s translation into Ubbi Dubbi
    So every vowel (a, e, i, o, or u) is prefaced with ub.
    octopus == > uboctubopubus. elephant == > ubelubephubant.
    """
    out = ['ub' + char.lower() if char.lower() in 'aeiou'
     else char.lower() for char in word]
    if word[0].istitle():
        out[0] = out[0].capitalize()
    return ''.join(out)





print(ubbi_dubbi('Elephant'))
