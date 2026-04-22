#print("Hello World")
from textnode import TextType, TextNode

def main():
    Node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(Node)

main()