from textnode import (
    text_node_to_html_node,
    text_to_textnodes,
)
from parentnode import ParentNode

BLOCK_TYPE_HEADING = "heading"
BLOCK_TYPE_CODE = "code"
BLOCK_TYPE_QUOTE = "quote"
BLOCK_TYPE_UNORDERED_LIST = "unordered_list"
BLOCK_TYPE_ORDERED_LIST = "ordered_list"
BLOCK_TYPE_PARAGRAPH = "paragraph"


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
        return ""
    if is_heading(block):
        return BLOCK_TYPE_HEADING
    if is_code(block):
        return BLOCK_TYPE_CODE
    lines = block.splitlines()
    if is_quote(lines):
        return BLOCK_TYPE_QUOTE
    if is_unordered_list(lines):
        return BLOCK_TYPE_UNORDERED_LIST
    if is_ordered_list(lines):
        return BLOCK_TYPE_ORDERED_LIST
    return BLOCK_TYPE_PARAGRAPH


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
        case BLOCK_TYPE_HEADING:
            return heading_to_html_node(block)
        case BLOCK_TYPE_CODE:
            pass
        case BLOCK_TYPE_QUOTE:
            pass
        case BLOCK_TYPE_UNORDERED_LIST:
            pass
        case BLOCK_TYPE_ORDERED_LIST:
            pass
        case BLOCK_TYPE_PARAGRAPH:
            pass
        case _:
            pass


# TODO: will create appropriate ParentNode with children from text_to_children() also will call to_html()
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
    lines = 


def ordered_list_to_html_node(block):
    pass


def paragraph_to_html_node(block):
    pass


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]
