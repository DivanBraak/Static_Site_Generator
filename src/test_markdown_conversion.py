import unittest

from textnode import TextNode, TextType
from markdown_conversion import split_nodes_delimiter,extract_markdown_images,extract_markdown_links


class TestSplitNodesDelimiter(unittest.TestCase):
    #Tests no delimiters
    def test_no_delimiters(self):
        node = TextNode("placeholder text", TextType.TEXT)

        result = split_nodes_delimiter([node], "`", TextType.TEXT)

        self.assertEqual(result, [
            TextNode("placeholder text", TextType.TEXT)
        ])

    #Tests no end delimiter
    def test_no_closing_delimiters(self):
        node = TextNode("This has a **bold line",TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.TEXT)

    #Tests normal usage
    def test_normal_usage(self):
        node = TextNode("This has a **bold** line",TextType.TEXT)

        result = split_nodes_delimiter([node],"**",TextType.BOLD)

        self.assertEqual(result,[
            TextNode("This has a ",TextType.TEXT),
            TextNode("bold",TextType.BOLD),
            TextNode(" line",TextType.TEXT)
        ])

    #Tests sending in multiple nodes
    def test_multiple_nodes(self):
        nodes = [
            TextNode("First node with `code` inside", TextType.TEXT),
            TextNode("Second node, no delimiters", TextType.TEXT),
            TextNode("Third node with `more code` here", TextType.TEXT),
        ]

        result = split_nodes_delimiter(nodes, "`", TextType.CODE)

        self.assertEqual(result, [
            TextNode("First node with ",TextType.TEXT),
            TextNode("code",TextType.CODE),
            TextNode(" inside",TextType.TEXT),
            TextNode("Second node, no delimiters",TextType.TEXT),
            TextNode("Third node with ",TextType.TEXT),
            TextNode("more code",TextType.CODE),
            TextNode(" here",TextType.TEXT)
        ])

    #Tests using not text type
    def test_not_text(self):
        node = TextNode("LINK",TextType.LINK,"www.google.com")

        result = split_nodes_delimiter([node],':',TextType.LINK)

        self.assertEqual(result, [
            TextNode("LINK",TextType.LINK,"www.google.com")
        ])

class test_image_and_link_extractors(unittest.TestCase):
    #Test image extraction
    def test_extract_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )

        self.assertEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    #Test image extraction
    def test_extract_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )

        self.assertEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

if __name__ == "__main__":
    unittest.main()
