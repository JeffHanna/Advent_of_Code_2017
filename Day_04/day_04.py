# -*- coding: utf-8 -*-
"""
--- Day 4: High-Entropy Passphrases ---

A new system policy has been put in place that requires all accounts to use a passphrase instead
of simply a password. A passphrase consists of a series of words (lowercase letters) separated
by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?


--- Part Two ---

For added security, yet another system policy has been put in place. Now, a valid passphrase must
contain no two words that are anagrams of each other - that is, a passphrase is invalid if any
word's letters can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the
first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming
another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?
"""

import itertools


def validate_passphrases(passphrases):
    """
    Password validation for Part1. Converting each row to a set removes duplicates.
    Therefore, if the length of the set and the length of the row differ, a duplicate
    passphrase exists.
    """

    valid_passphrases = 0

    for line in passphrases:
        parts = line.strip().split(' ')
        if len(set(parts)) == len(parts):
            valid_passphrases += 1

    return valid_passphrases


def validate_no_anagram_passphrases(passphrases):
    """
    Password validation for Part 1. Converting each element in a row to a set and comparing the sets
    will indicate if any two elements share the exact same letters, indicating an anagram.
    """

    invalid_passphrases = 0

    for line in passphrases:
        parts = line.strip().split(' ')
        for word_1, word_2 in itertools.combinations(parts, 2):
            if set(word_1) == set(word_2):
                invalid_passphrases += 1
                break

    return len(passphrases) - invalid_passphrases



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        PASSPHRASES = f.readlines()

    print(validate_passphrases(PASSPHRASES))
    print(validate_no_anagram_passphrases(PASSPHRASES))
