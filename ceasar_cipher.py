#!/usr/bin/env python3
# coding=utf-8

"""
Caesar Cipher Utility Function

This function is responsible for shifting characters in a given text
to perform both encryption and decryption using the Caesar cipher technique.
"""

def shift_txt(txt: str, shift: int) -> str:
    digits = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{};:,.<>/?"
    result = ""
    for char in txt:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif char in digits:
            result += digits[(digits.index(char) + shift) % 10]
        elif char in symbols:
            result += symbols[(symbols.index(char) + shift) % len(symbols)]
        else:
            result += char
    return result
