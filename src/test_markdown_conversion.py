import unittest

from textnode import TextNode, TextType
from markdown_conversion import split_nodes_delimiter,extract_markdown_images,extract_markdown_links,split_nodes_image,split_nodes_link


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

class test_image_and_link_splitting(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link to](https://i.imgur.com/zjjcJKZ.png) and another [link to](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link to", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link to", TextType.LINK, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes
        )

if __name__ == "__main__":
    unittest.main()
