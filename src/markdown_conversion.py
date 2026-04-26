import re
from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        
        #Checks if the node is text
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if not delimiter in node.text:
            new_nodes.append(node)
            continue
        
        #Splits the text into lines of text based on delimiter
        lines = node.text.split(delimiter)

        if len(lines)%2 == 0: #
            raise Exception("ERROR: No end delimiter found")

        for i in range(len(lines)):
            if lines[i] != '':
                if i%2 == 0: #is even
                    new_nodes.append(TextNode(lines[i],TextType.TEXT))
                else: #is odd
                    new_nodes.append(TextNode(lines[i], text_type))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
