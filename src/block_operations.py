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
