from enum import Enum
from textnode import (
    text_node_to_html_node,
    text_to_textnodes,
)
from parentnode import ParentNode


class BlockType(Enum):
    NONE = ""
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    PARAGRAPH = "paragraph"


def markdown_to_blocks(markdown):
    if not markdown:
        return []
    split_markdown = markdown.split("\n\n")
    return list(
        filter(
            lambda line: line,
            map(lambda line: line.strip(), split_markdown),
        )
    )


def block_to_block_type(block):
    if not block:
        return BlockType.NONE
    if is_heading(block):
        return BlockType.HEADING
    if is_code(block):
        return BlockType.CODE
    lines = block.splitlines()
    if is_quote(lines):
        return BlockType.QUOTE
    if is_unordered_list(lines):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(lines):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def is_heading(block):
    headings = (
        "# ",
        "## ",
        "### ",
        "#### ",
        "##### ",
        "###### ",
    )
    return block.startswith(headings)


def is_code(block):
    return block.startswith("```") and block.endswith("```")


def is_quote(lines):
    return all(line.startswith(">") for line in lines)


def is_unordered_list(lines):
    return all(line.startswith(("* ", "- ")) for line in lines)


def is_ordered_list(lines):
    return all(line.startswith(f"{i}. ") for i, line in enumerate(lines, 1))


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(block)
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case _:
            raise ValueError("Invalid block type")


def heading_to_html_node(block):
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    children = text_to_children(block[count + 1 :])
    return ParentNode(f"h{count}", children)


def code_to_html_node(block):
    text = block[4:-3]
    children = text_to_children(text)
    code_tag_html_node = ParentNode("code", children)
    return ParentNode("pre", [code_tag_html_node])


def quote_to_html_node(block):
    lines = [line[2:] for line in block.splitlines()]
    children = text_to_children(" ".join(lines))
    return ParentNode("blockquote", children)


def unordered_list_to_html_node(block):
    children = [
        ParentNode("li", text_to_children(line[2:])) for line in block.splitlines()
    ]
    return ParentNode("ul", children)


def ordered_list_to_html_node(block):
    children = [
        ParentNode("li", text_to_children(line[3:])) for line in block.splitlines()
    ]
    return ParentNode("ol", children)


def paragraph_to_html_node(block):
    lines = block.splitlines()
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]
