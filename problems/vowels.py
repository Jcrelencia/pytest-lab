"""
PROBLEM 3
================================

Write a function that returns the NUMBER of vowels in `text`.

    count_vowels("hello")  ->  2
    count_vowels("xyz")    ->  0
"""


def count_vowels(text: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in text."""
    vowels = "aeiouAEIOU"

    count = 0

    for letter in text:
        if letter in vowels:
            count += 1
    return count
  
    pass
