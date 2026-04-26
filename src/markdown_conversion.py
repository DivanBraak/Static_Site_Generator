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

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        node_text = node.text
        #Extracts images
        images = extract_markdown_images(node.text)

        for image in images:
            #Splits the text into text before and after image
            lines = node_text.split(f"![{image[0]}]({image[1]})",1)

            #Adds text to
            new_nodes.append(TextNode(lines[0],TextType.TEXT))
            new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))

            #sets text to unparsed text
            node_text = lines[1]
        
        if node_text != '':
            new_nodes.append(TextNode(node_text,TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        node_text = node.text
        #Extracts images
        links = extract_markdown_links(node.text)

        for link in links:
            #Splits the text into text before and after link
            lines = node_text.split(f"[{link[0]}]({link[1]})",1)

            #Adds text to
            new_nodes.append(TextNode(lines[0],TextType.TEXT))
            new_nodes.append(TextNode(link[0],TextType.LINK,link[1]))

            #sets text to unparsed text
            node_text = lines[1]
        
        if node_text != '':
            new_nodes.append(TextNode(node_text,TextType.TEXT))

    return new_nodes
