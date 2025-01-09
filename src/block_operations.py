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
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BLOCK_TYPE_HEADING:
                pass
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
