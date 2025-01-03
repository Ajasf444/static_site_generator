from enum import Enum
from leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})\n"


def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    text = text_node.text
    url = text_node.url

    match text_type:
        case TextType.TEXT:
            return LeafNode(None, text)
        case TextType.BOLD:
            return LeafNode("b", text)
        case TextType.ITALIC:
            return LeafNode("i", text)
        case TextType.CODE:
            return LeafNode("code", text)
        case TextType.LINK:
            return LeafNode("a", text)
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": url, "alt": text})
        case _:
            raise ValueError("Invalid TextType")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if not old_nodes:
        return new_nodes
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        for i, text in enumerate(split_text):
            if not text:
                continue
            if i % 2 == 0:
                new_node = TextNode(text, TextType.TEXT)
            else:
                new_node = TextNode(text, text_type)
            new_nodes.append(new_node)
    return new_nodes
