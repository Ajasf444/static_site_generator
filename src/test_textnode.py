import unittest

from textnode import (
    TextNode,
    TextType,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_node_to_html_node,
)
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
    def test_text_type(self):
        text_node = TextNode("normal text", TextType.TEXT)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode(None, "normal text"))

    def test_bold_type(self):
        text_node = TextNode("bold text", TextType.BOLD)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("b", "bold text"))

    def test_italic_type(self):
        text_node = TextNode("italic text", TextType.ITALIC)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("i", "italic text"))

    def test_code_type(self):
        text_node = TextNode("code", TextType.CODE)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("code", "code"))

    def test_link_type(self):
        text_node = TextNode("link", TextType.LINK)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node, LeafNode("a", "link"))

    def test_image_type(self):
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


class TestSplitNodesImage(unittest.TestCase):
    def test_empty_old_nodes(self):
        self.assertEqual(split_nodes_image([]), [])

    def test_single_node_multiple_images(self):
        node = TextNode(
            "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        output = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(split_nodes_image([node]), output)

    def test_multiple_nodes_multiple_images(self):
        node_1 = TextNode(
            "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        node_2 = TextNode(
            "This is another image ![blah](https://www.blah.com) and ![blah_2](https://www.blah_blah.com/baconator_fries) Tahm Kench",
            TextType.TEXT,
        )
        output = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode("This is another image ", TextType.TEXT),
            TextNode("blah", TextType.IMAGE, "https://www.blah.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "blah_2", TextType.IMAGE, "https://www.blah_blah.com/baconator_fries"
            ),
            TextNode(" Tahm Kench", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_image([node_1, node_2]), output)


class TestSplitNodesLink(unittest.TestCase):
    def test_empty_old_nodes(self):
        self.assertEqual(split_nodes_link([]), [])

    def test_single_node_multiple_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        output = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(split_nodes_link([node]), output)

    def test_multiple_nodes_multiple_links(self):
        node_1 = TextNode(
            "This is text with an image [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        node_2 = TextNode(
            "This is another image [blah](https://www.blah.com) and [blah_2](https://www.blah_blah.com/baconator_fries) Tahm Kench",
            TextType.TEXT,
        )
        output = [
            TextNode("This is text with an image ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode("This is another image ", TextType.TEXT),
            TextNode("blah", TextType.LINK, "https://www.blah.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "blah_2", TextType.LINK, "https://www.blah_blah.com/baconator_fries"
            ),
            TextNode(" Tahm Kench", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_link([node_1, node_2]), output)


if __name__ == "__main__":
    unittest.main()
