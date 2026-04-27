from enum import Enum

from htmlnode import HTMLNode,ParentNode,LeafNode
from textnode import TextNode,text_node_to_html_node,TextType
from markdown_conversion import text_to_textnodes

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

#TURNING BLOCKS INTO HTML NODES
def markdown_to_html_nodes(markdown):
    #Split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        node = convert_block_to_html_node(block)
        block_nodes.append(node)

    return ParentNode("div", block_nodes)

def convert_block_to_html_node(block):
    block_type = block_to_block_type(block)

    #PARAGRAPH LOGIC
    if block_type == BlockType.PARAGRAPH:
        children = text_to_children(remove_newlines(block))
        node = ParentNode('p',children)

    if block_type == BlockType.HEADING:
        children = text_to_children(remove_hashtags(block))
        node = ParentNode('h'+which_heading(block),children)

    if block_type == BlockType.QUOTE:
        children = text_to_children(remove_quote(block))
        node = ParentNode('blockquote',children)

    if block_type == BlockType.UNORDERED_LIST:
        children = text_to_children(ul_format(block))
        node = ParentNode('ul',children)

    if block_type == BlockType.ORDERED_LIST:
        children = text_to_children(ol_format(block))
        node = ParentNode('ol',children)

    if block_type == BlockType.CODE:
        text_node = TextNode(code_format(block),TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        code_node = ParentNode('code',[html_node])
        node = ParentNode('pre',[code_node])
    
    return node

#Takes raw text (md) and parses it into text_nodes. Then the text nodes are turned into leaf nodes (html nodes) and returned.
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    leaf_nodes = []

    for node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(node))

    return leaf_nodes

#---------------------HELPER FUNCTIONS---------------------

#Takes a heading bloc kand find out the heading level
def which_heading(block):
    #HEADING LEVEL
    count = (len(block) - len(block.lstrip('#')))
    return str(count)

#Remove newlines from paragraphs
def remove_newlines(block):
    lines = block.split('\n')
    new_lines = ' '.join(lines)
    return new_lines

#Remove hashtags from headings
def remove_hashtags(block):
    block = block.lstrip('#')
    block = block.lstrip()
    return block

#Clean up quotes
def remove_quote(block):
    lines = block.split('\n')
    new_lines = []
    for line in lines:
        line = line.lstrip('>')
        line = line.lstrip()   
        new_lines.append(line)
    lines = ' '.join(new_lines)
    return lines     

#Format unordered lists
def ul_format(block):
    lines = block.split('\n')
    new_lines = []
    for line in lines:
        line = line[2:]
        line = "<li>"+line+"</li>"
        new_lines.append(line)
    lines = ''.join(new_lines)
    return lines

#Format ordered lists
def ol_format(block):
    lines = block.split('\n')
    new_lines = []
    for line in lines:
        line = line[3:]
        line = "<li>"+line+"</li>"
        new_lines.append(line)
    lines = ''.join(new_lines)
    return lines

#Code format
def code_format(block):
    block = block[4:]
    block = block[:-3]
    return block
