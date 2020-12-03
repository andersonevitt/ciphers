"""Unit tests for caesar ciphers"""

import unittest
import sys

from ciphers import caesar

example = "A simple sentence."

class CaesarTests(unittest.TestCase):

    def test_cipher(self):
        self.assertEqual(caesar.cipher(example, 10), "K cswzvo coxdoxmo.")

    def test_decipher(self):
        self.assertEqual(caesar.decipher("K cswzvo coxdoxmo.", 10), "A simple sentence.")

if __name__ == "__main__":

    unittest.main()

