import unittest

from inline_operations import extract_markdown_images, extract_markdown_links


class TestExtractMarkdownImages(unittest.TestCase):
    def test_no_images(self):
        text = "blah"
        output = []
        self.assertEqual(extract_markdown_images(text), output)

    def test_single_image(self):
        text = "![alt text](https://google.com/blah.gif)"
        output = [("alt text", "https://google.com/blah.gif")]
        self.assertEqual(extract_markdown_images(text), output)

    def test_multiple_images(self):
        text = "![alt text 1](https://google.com/blah.gif) Tahm Kench ![alt text 2](https://bing.com/blah_2.gif)"
        output = [
            ("alt text 1", "https://google.com/blah.gif"),
            ("alt text 2", "https://bing.com/blah_2.gif"),
        ]
        self.assertEqual(extract_markdown_images(text), output)


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_no_links(self):
        text = "blah"
        output = []
        self.assertEqual(extract_markdown_links(text), output)

    def test_single_link(self):
        text = "[alt text](https://google.com/blah.gif)"
        output = [("alt text", "https://google.com/blah.gif")]
        self.assertEqual(extract_markdown_links(text), output)

    def test_multiple_links(self):
        text = "[alt text 1](https://google.com/blah.gif) Tahm Kench [alt text 2](https://bing.com/blah_2.gif)"
        output = [
            ("alt text 1", "https://google.com/blah.gif"),
            ("alt text 2", "https://bing.com/blah_2.gif"),
        ]
        self.assertEqual(extract_markdown_links(text), output)


if __name__ == "__main__":
    unittest.main()
