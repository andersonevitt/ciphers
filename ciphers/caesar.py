"""Caesar ciphering and deciphering."""

import string


def cipher(input: str, shift: int = 1) -> str:
    """Caesar ciphers an input.

    Args:
        input - The input to be ciphered
        shift - The amount of characters to shift by, defaults to 1

    Returns:
        The ciphered output
    """

    # The output
    result = ""

    for ch in input:
        # Check if ch is part of the alphabet, pass if not
        if ch.isalpha():
            # handle uppercase
            if ch.isupper():
                result += chr((ord(ch) + shift - 65) % 26 + 65)
            # handle lowercase
            else:
                result += chr((ord(ch) + shift - 97) % 26 + 97)
        # if isn't alphanumeric ignore it
        else:
            result += ch
    return result


def decipher(input, shift = 1):
    """Deciphers a caesar ciphered input.

    Args:
        input - The input to be deciphered
        shift - The amount of characters to shift by, defaults to 1

    Returns:
        The deciphered output
    """

    # Output
    result = ""

    for ch in input:
        # Check if ch is part of the alphabet, pass if not
        if ch.isalpha():
            # handle uppercase
            if ch.isupper():
                result += chr((ord(ch) - shift - 65) % 26 + 65)
            # handle lowercase
            else:
                result += chr((ord(ch) - shift - 97) % 26 + 97)
        # if isn't alphanumeric ignore it
        else:
            result += ch

    return result
