import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode("p")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        node = HTMLNode("a", "click me", None, {"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_print_HTMLNode(self):
        node = HTMLNode("p", "hello", None, None)
        expected = "\n".join([
        "xxxxxxxxxxxxxxxxxxHTML NODExxxxxxxxxxxxxxxxxxxxxxxx",
        "TAG: p",
        "VALUE: hello",
        "CHILDREN: None",
        "PROPS: None",
        "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ])
        self.assertEqual(repr(node), expected)