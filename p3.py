def letter_count(string):
    letterdict = {}
    for letter in string:
        letterdict[letter] = 0
    for letter in string:
        letterdict[letter] += 1
    return letterdict
