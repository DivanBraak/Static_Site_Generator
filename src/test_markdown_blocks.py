import unittest

from markdown_blocks import markdown_to_blocks,block_to_block_type,BlockType,markdown_to_html_nodes,extract_title

class test_blocks(unittest.TestCase):
    def test_normal_usage(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_many_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_whitespace(self):
        md = """
    This is **bolded** paragraph       

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line   

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_empty_input(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            []
        )

    def test_single_block(self):
        md = """
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line"]
        )

class test_block_to_block_type(unittest.TestCase):
    #HEADING TESTS
    def test_heading1(self):
        input = "# Heading 1"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.HEADING)

    def test_heading6(self):
        input = "###### Heading 6"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.HEADING)

    def test_heading_too_many_hash(self):
        input = "####### Not a heading"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_heading_no_space(self):
        input = "#No space"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    #CODE TESTS
    def test_code(self):
        input = "```\nprint('hi')\n```"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.CODE)

    def test_multiline_code(self):
        input = "```\ncode block\nmore code\n```"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.CODE)

    def test_code_wrong_ident(self):
        input = "``\nprint('hi')\n``"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    #QUOTE TESTS
    def test_quote(self):
        input = ">quote"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.QUOTE)

    def test_quote_space(self):
        input = "> quote\n> another quote"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.QUOTE)

    def test_heading_too_many_hash(self):
        input = "> good\nnot a quote"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    #UNORDERED LIST TESTS
    def test_ul(self):
        input = "- one"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_ul_multi(self):
        input = "- one\n- two\n- three"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_heading_too_many_hash(self):
        input = "- one\nnot a list item"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    #ORDERED LIST TESTS
    def test_ol(self):
        input = "1. one"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_ol_multi(self):
        input = "1. one\n2. two\n3. three"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_ol_numberskip(self):
        input = "1. one\n3. three"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_ol_starts_wrong(self):
        input = "2. starts wrong"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    #PARAGRAPH TESTS
    def test_paragraph(self):
        input = "just a normal paragraph"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_paragraph_multi(self):
        input = "this is text\nthat does not match any special block"

        block = markdown_to_blocks(input)[0]

        result = block_to_block_type(block)

        self.assertEqual(result, BlockType.PARAGRAPH)

class test_markdown_to_html_block_nodes(unittest.TestCase):
    def test_complete_test(self):
        md = md = """
# Heading 1

## Heading 2 with **bold**

### Heading 3 with _italic_

This is a normal paragraph with **bold**, _italic_, and `code` inline.

This is another paragraph
that spans multiple lines
and should collapse to spaces.

> This is a quote block
> that spans multiple lines
> and has **bold** text inside.

- unordered item one
- unordered item two with _italic_
- unordered item three

1. ordered item one
2. ordered item two with `code`
3. ordered item three

```
this is a code block
it should _not_ parse **inline** markdown
keep newlines intact
```
"""
 
        node = markdown_to_html_nodes(md)
        html = node.to_html()

        expected = """
<div><h1>Heading 1</h1><h2>Heading 2 with <b>bold</b></h2><h3>Heading 3 with <i>italic</i></h3><p>This is a normal paragraph with <b>bold</b>, <i>italic</i>, and <code>code</code> inline.</p><p>This is another paragraph that spans multiple lines and should collapse to spaces.</p><blockquote>This is a quote block that spans multiple lines and has <b>bold</b> text inside.</blockquote><ul><li>unordered item one</li><li>unordered item two with <i>italic</i></li><li>unordered item three</li></ul><ol><li>ordered item one</li><li>ordered item two with <code>code</code></li><li>ordered item three</li></ol><pre><code>this is a code block
it should _not_ parse **inline** markdown
keep newlines intact
</code></pre></div>
""".strip()

        self.assertEqual(
            html,
            expected
        )
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_heading1(self):
        md = """
# Heading 1
"""

        node = markdown_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1></div>",
        )

    def test_heading2(self):
        md = """
## Heading 2
"""

        node = markdown_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Heading 2</h2></div>",
        )

    def test_heading_with_inline_bold(self):
        md = """
## Heading 2 with **bold**
"""

        node = markdown_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>Heading 2 with <b>bold</b></h2></div>",
        )

    def test_empty_markdown(self):
        md = """
"""
        self.assertRaises(ValueError,markdown_to_html_nodes,md)

    def test_all_headings(self):
        md = """
# Heading 1

## Heading 2 with **bold** and _italic_

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6
"""

        node = markdown_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2 with <b>bold</b> and <i>italic</i></h2><h3>Heading 3</h3><h4>Heading 4</h4><h5>Heading 5</h5><h6>Heading 6</h6></div>",
        )

    def test_wrong_heading(self):
        md = """
####### Not a heading, just a paragraph with seven hashes
"""

        node = markdown_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>####### Not a heading, just a paragraph with seven hashes</p></div>",
        )

    def test_unordered_list(self):
        md = """
- Unordered item one
- Unordered item two with `code`
- Unordered item three with [a link](https://example.com)
"""

        node = markdown_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>Unordered item one</li><li>Unordered item two with <code>code</code></li><li>Unordered item three with <a href="https://example.com">a link</a></li></ul></div>'
        )

    def test_unordered_list(self):
        md = """
1. Ordered item one
2. Ordered item two with **bold**
3. Ordered item three with _italic_
"""

        node = markdown_to_html_nodes(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ol><li>Ordered item one</li><li>Ordered item two with <b>bold</b></li><li>Ordered item three with <i>italic</i></li></ol></div>'
        )
class test_title_extractor(unittest.TestCase):
    def test_normal_usage(self):
        md = """
# This is the Title

This is a paragraph
"""
        result = extract_title(md)
        self.assertEqual(result,"This is the Title")

    def test_more_hash_and_whitespace(self):
        md = """
# ## This is the Title       

This is a paragraph
"""
        result = extract_title(md)
        self.assertEqual(result,"## This is the Title")

    def test_no_title(self):
        md = """
## This is not the Title

This is a paragraph
"""
        self.assertRaises(Exception,extract_title,md)

    def test_bad_formatting(self):
        md = """
# This is the Title
This is a paragraph
"""
        result = extract_title(md)
        self.assertEqual(result,"This is the Title")


    def test_bad_formatting2(self):
        md = """# Real Title

## Subheading
Some text
"""
        result = extract_title(md)
        self.assertEqual(result,"Real Title")



if __name__ == "__main__":
    unittest.main()