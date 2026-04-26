def markdown_to_blocks(markdown):
    raw_blocks = markdown.split('\n\n')
    blocks = []

    for block in raw_blocks:
        if block != '':
            blocks.append(block.strip())  

    return blocks