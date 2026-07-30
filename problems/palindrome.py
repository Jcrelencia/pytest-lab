"""
PROBLEM 2
=========================================================

Write a function that returns True if `text` reads the same forwards
and backwards, and False otherwise.

    is_palindrome("racecar")  ->  True
    is_palindrome("hello")    ->  False
"""

def is_palindrome(text: str) -> bool:
    """Return True if text reads the same forwards and backwards."""
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def is_palindrome_list(numbers: list) -> bool:
    """Return True if the list reads the same forwards and backwards."""
    return numbers == numbers[::-1]

