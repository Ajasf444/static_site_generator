import unittest

from block_operations import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
    markdown_to_html_node,
)
from parentnode import ParentNode


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_multiple_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        html = markdown_to_html_node(markdown).to_html()
        output = "<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>"

        self.assertEqual(html, output)

    def test_multiple_blocks_with_extraneous_newlines(self):
        markdown = """# This is a heading




This is a paragraph of text. It has some **bold** and *italic* words inside of it.




* This is the first list item in a list block
* This is a list item
* This is another list item


"""
        html = markdown_to_html_node(markdown).to_html()
        output = "<div><h1>This is a heading</h1><p>This is a paragraph of text. It has some <b>bold</b> and <i>italic</i> words inside of it.</p><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>"

        self.assertEqual(html, output)


class TestMarkdownToBlocks(unittest.TestCase):
    def test_empty_markdown(self):
        markdown = ""
        output = []
        self.assertEqual(markdown_to_blocks(markdown), output)

    def test_extraneous_newlines(self):
        markdown = """# This is a heading




This is a paragraph of text. It has some **bold** and *italic* words inside of it.




* This is the first list item in a list block
* This is a list item
* This is another list item


"""

        output = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]
        self.assertEqual(markdown_to_blocks(markdown), output)

    def test_multiple_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        output = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]
        self.assertEqual(markdown_to_blocks(markdown), output)


class TestBlockToBlockType(unittest.TestCase):
    def test_empty_block(self):
        block = ""
        self.assertEqual(block_to_block_type(block), BlockType.NONE)

    def test_none_block(self):
        block = None
        self.assertEqual(block_to_block_type(block), BlockType.NONE)

    def test_heading(self):
        block = "# single heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "## single heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "### single heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "#### single heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "##### single heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "###### single heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code_block(self):
        block = "```This is code.```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = ">First Line.\n" ">Second Line.\n" ">Third Line.\n"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = (
            "* First item.\n"
            "- Second item.\n"
            "- Third item.\n"
            "* Fourth item.\n"
            "- Fifth item.\n"
        )
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. First item.\n" "2. Second item.\n" "3. Third item.\n"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        block = "This is arbitrary text.\nHow do you do?"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
