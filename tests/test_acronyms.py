import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import acronyms


class TestAcronyms(unittest.TestCase):

    def test_is_valid_short_form(self):
        self.assertTrue(acronyms.is_valid_short_form("abc"))
        self.assertTrue(acronyms.is_valid_short_form("1abc"))
        self.assertTrue(acronyms.is_valid_short_form("(abc"))
        self.assertTrue(acronyms.is_valid_short_form("abc"))
        self.assertFalse(acronyms.is_valid_short_form("123"))
        self.assertFalse(acronyms.is_valid_short_form("(123"))

    def test_has_letter(self):
        self.assertTrue(acronyms.has_letter("abc"))
        self.assertTrue(acronyms.has_letter("123a"))
        self.assertFalse(acronyms.has_letter("123"))

    def test_has_capital(self):
        self.assertTrue(acronyms.has_capital("Abc"))
        self.assertTrue(acronyms.has_capital("ABC"))
        self.assertFalse(acronyms.has_capital("abc"))
        self.assertFalse(acronyms.has_capital("123"))

    def test_extract_pairs(self):
        sentence = """
            Three aspects of the involvement of tumor necrosis factor 
            in human immunodeficiency virus (HIV) pathogenesis were examined.
        """
        pairs = acronyms.extract_pairs(sentence)
        self.assertListEqual(pairs, [{"acronym": "HIV", "definition": "human immunodeficiency virus"}])

    def test_best_long_form(self):
        self.assertTrue(True)

    def test_match_pair(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
