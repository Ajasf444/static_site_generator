import unittest

from textnode import TextNode, TextType, split_nodes_delimiter, text_node_to_html_node
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_uneq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_uneq_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertNotEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        text_node = TextNode("normal text", TextType.TEXT)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode(None, "normal text"))

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("bold text", TextType.BOLD)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("b", "bold text"))

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("italic text", TextType.ITALIC)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("i", "italic text"))

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("code", TextType.CODE)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("code", "code"))

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("link", TextType.LINK)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("a", "link"))

    def test_text_node_to_html_node_image(self):
        text_node = TextNode("alt text", TextType.IMAGE, "https://dummy.jpg")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(
            leaf_node,
            LeafNode("img", "", {"src": "https://dummy.jpg", "alt": "alt text"}),
        )


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_empty_old_nodes(self):
        self.assertEqual(split_nodes_delimiter([], "`", TextType.CODE), [])

    def test_non_text_node(self):
        node = TextNode("Tahm Kench", TextType.CODE)
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), [node])

    def test_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        output = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), output)

    def test_two_code_blocks(self):
        node = TextNode("`code block a` `code block b`", TextType.TEXT)
        output = [
            TextNode("code block a", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("code block b", TextType.CODE),
        ]
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), output)


if __name__ == "__main__":
    unittest.main()
