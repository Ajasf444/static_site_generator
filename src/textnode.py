from enum import Enum
from leafnode import LeafNode
from inline_operations import extract_markdown_images, extract_markdown_links


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
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_text = old_node.text.split(delimiter)
        for i, text in enumerate(split_text):
            if not text:
                continue
            if i % 2 == 0:
                new_node = TextNode(text, TextType.TEXT)
            else:
                new_node = TextNode(text, text_type)
            new_nodes.append(new_node)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    if not old_nodes:
        return new_nodes
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for description, url in images:
            split_text = remaining_text.split(f"![{description}]({url})", 1)
            text, remaining_text = split_text[0], split_text[1]
            if text:
                new_nodes.append(TextNode(text, TextType.TEXT))
            new_nodes.append(TextNode(description, TextType.IMAGE, url))
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    if not old_nodes:
        return new_nodes
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for description, url in links:
            split_text = remaining_text.split(f"[{description}]({url})", 1)
            text, remaining_text = split_text[0], split_text[1]
            if text:
                new_nodes.append(TextNode(text, TextType.TEXT))
            new_nodes.append(TextNode(description, TextType.LINK, url))
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes
