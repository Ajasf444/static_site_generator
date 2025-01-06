def markdown_to_blocks(markdown):
    if not markdown:
        return []
    split_markdown = markdown.split("\n\n")
    return list(
        filter(
            lambda line: line,
            map(lambda line: line.strip("\n").strip(" "), split_markdown),
        )
    )


def block_to_block_type(block):
    if not block:
        return ""
    if is_heading(block):
        return "heading"
    if is_code(block):
        return "code"
    lines = block.splitlines()
    if is_quote(lines):
        return "quote"
    if is_unordered_list(lines):
        return "unordered_list"
    if is_ordered_list(lines):
        return "ordered_list"
    return "paragraph"


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
