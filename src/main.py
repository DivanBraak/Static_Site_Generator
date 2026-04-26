#print("Hello World")
from textnode import TextType, TextNode
from htmlnode import HTMLNode
from markdown_conversion import *

def main():
    #Node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    #print(Node)
    #HTML_Node = HTMLNode("a", "click me", None, {"href": "https://example.com"})
    #print(HTML_Node.props_to_html())
    extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
    pass

main()