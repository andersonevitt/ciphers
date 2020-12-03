"""Unit tests for rot-13 ciphers"""

import unittest
import sys

from ciphers import rot13

example = "A simple sentence."


class Rot13Tests(unittest.TestCase):
    def test_cipher(self):
        self.assertEqual(rot13.cipher(example), "N fvzcyr fragrapr.")

    def test_decipher(self):
        self.assertEqual(rot13.decipher("N fvzcyr fragrapr."),
                         "A simple sentence.")


if __name__ == "__main__":
    unittest.main()
