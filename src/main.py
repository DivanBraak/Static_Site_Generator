#print("Hello World")
from textnode import TextType, TextNode
from htmlnode import HTMLNode
from markdown_conversion import *
from markdown_blocks import *

def main():
    md = """
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
    print(html)
    pass

main()