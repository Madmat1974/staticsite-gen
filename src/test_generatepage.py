import unittest
from extraction import *

class TestTitleExtraction(unittest.TestCase):
    def test_find_title(self):
        md = "# Tolkien Fan Club"
        md2 = extract_title(md)
        self.assertEqual(md2, "Tolkien Fan Club")

if __name__ == "__main__":
    unittest.main()