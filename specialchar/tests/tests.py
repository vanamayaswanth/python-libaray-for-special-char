import unittest
from specialchar import SpecialChar

class TestSpecialChar(unittest.TestCase):
    def test_special_char(self):
        specialChar = SpecialChar()
        specialChar.char = "!"
        specialChar.name = "exclamation mark"
        self.assertEqual(specialChar.name, "exclamation mark")

if __name__ == "__main__":
    unittest.main()
