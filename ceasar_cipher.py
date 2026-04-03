#!/usr/bin/env python3
# coding=utf-8

"""
Caesar Cipher Utility Function

This function is responsible for shifting characters in a given text
to perform both encryption and decryption using the Caesar cipher technique.
"""

def shift_txt(txt: str, shift: int) -> str:
    """
    This function shift it is responsible for shifting characters in a given text
    for encryption it will Add the text and for decrypt it will subtract the encrypted text.
    """

    digits = "0123456789"
    symbols = "!@#$%^&*()_+-=[]{};:,.<>/?|~`"
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



def encryption(txt: str, shift: int) -> str:
    """
    This function performs encryption using the Caesar cipher technique.
    It will add the text for encryption.
    """
    Adding this line for the example for kt
    return shift_txt(txt, shift)


def decryption(txt: str, shift: int) -> str:
    """
    This function performs decryption using the Caesar cipher technique.
    It will Sub the text for encryption.
    """
    pass
    return shift_txt(txt, -shift)
    sam = "Hello"
    enc = encryption(sam, -shift)
    dec = decryption(enc, -shift)

if __name__ == '__main__':
    txt = input("Enter the text: ")
    shift = int(input("Enter the shift number: "))

    enc= encryption(txt, shift)
    print(enc)
    dec = decryption(enc, shift)
    print(dec)
