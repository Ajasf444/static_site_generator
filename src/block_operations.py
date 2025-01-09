block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"
block_type_paragraph = "paragraph"


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
        return block_type_heading
    if is_code(block):
        return block_type_code
    lines = block.splitlines()
    if is_quote(lines):
        return block_type_quote
    if is_unordered_list(lines):
        return block_type_unordered_list
    if is_ordered_list(lines):
        return block_type_ordered_list
    return block_type_paragraph


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
            case block_type_heading:
                pass
            case block_type_code:
                pass
            case block_type_quote:
                pass
            case block_type_unordered_list:
                pass
            case block_type_ordered_list:
                pass
            case block_type_paragraphblock_type_:
                pass
            case _:
                pass
