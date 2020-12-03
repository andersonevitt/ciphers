"""Rot13 ciphering and deciphering."""

from ciphers import caesar


def cipher(input):
    """Rot-13 ciphers an input.
    
    Args:
        input - The input string to be ciphered

    Returns:
        The ciphered output
    """
    return caesar.cipher(input, 13)


def decipher(input):
    """Deciphers a rot-13 ciphered input.

    Args:
        input - The input string to be deciphered

    Returns:
        The deciphered output
    """
    return caesar.decipher(input, 13)
