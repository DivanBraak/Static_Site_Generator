#print("Hello World")
from textnode import TextType, TextNode
from htmlnode import HTMLNode
from markdown_conversion import *
from markdown_blocks import *

def main():
    md = """
1. Ordered item one
2. Ordered item two with **bold**
3. Ordered item three with _italic_
"""

    node = markdown_to_html_nodes(md)
    html = node.to_html()
    print(html)
    pass

main()