import unittest

from page_generation import extract_title


class TestPageGeneration(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"
        output = "Hello"
        self.assertEqual(extract_title(markdown), output)

    def test_no_title(self):
        markdown = "Baconator Fries"
        self.assertRaises(Exception, lambda: extract_title(markdown))


if __name__ == "__main__":
    unittest.main()
