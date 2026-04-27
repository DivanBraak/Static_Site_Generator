from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"



def markdown_to_blocks(markdown):
    raw_blocks = markdown.split('\n\n')
    blocks = []

    for block in raw_blocks:
        if block != '':
            blocks.append(block.strip())  

    return blocks

def block_to_block_type(block):
    
    #HEADING CHECK (DONE)
    count = (len(block) - len(block.lstrip('#')))
    if 0 < count < 7:
        if count < len(block) and block[count] == " ":
            return BlockType.HEADING
    
    #CODE CHECK (DONE)
    if block.startswith('```\n') and block.endswith('```'):
        return BlockType.CODE
    
    #QUOTE CHECK (DONE)
    lines = block.split('\n')
    quote = True
    for line in lines:
        if not line.startswith('>'):
            quote = False
    if quote:
        return BlockType.QUOTE
    
    #UNORDERED_LIST CHECK 
    lines = block.split('\n')
    ul = True
    for line in lines:
        if not line.startswith('- '):
            ul = False
    if ul:
        return BlockType.UNORDERED_LIST
    
    #ORDERED_LIST CHECK 
    lines = block.split('\n')
    ol = True
    for i in range(len(lines)):
        expected = str((i+1))+'. '
        if not lines[i].startswith(expected):
            ol = False
    if ol:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH