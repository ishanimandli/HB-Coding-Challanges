"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:
    >>> import os, sys
    >>> all_words = [w.strip() for w in open(os.path.join(sys.path[0],'words.txt'))]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""
import os
import sys

def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""
    
    anagram_dict = make_anagram_dict(wordlist)
    max = -1
    max_key = ""
    for key in anagram_dict:
        if max < len(anagram_dict[key]):
            max = len(anagram_dict[key])
            max_key = key
    return sorted(anagram_dict[max_key])[0]

def make_anagram_dict(wordlist):
    anagram_dict = {}
    for word in wordlist:
        key = "".join(sorted(word))
        # print(key)
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = [word]
        # anagram_dict[key] = anagram_dict.get(key,list()).append(word)
    return anagram_dict


all_words = [w.strip() for w in open(os.path.join(sys.path[0],'words.txt'))]
find_most_anagrams_from_wordlist(all_words)

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
