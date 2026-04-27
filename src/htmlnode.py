"""
Defines HTMLNode, LeafNode and ParentNode. Letter 2 child classes of HTMLNode.
LeafNode does not have children
ParentNode does not have a value
"""

#--------------------------HTML NODE DECLARATION--------------------------
class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        output = ""
        for prop in self.props:
            output += f' {prop}="{self.props[prop]}"'
        return output
    
    def __repr__(self):
        print_lines = []
        print_lines.append("xxxxxxxxxxxxxxxxxxHTML NODExxxxxxxxxxxxxxxxxxxxxxxx")
        print_lines.append(f"TAG: {self.tag}")
        print_lines.append(f"VALUE: {self.value}")
        print_lines.append(f"CHILDREN: {self.children}")
        print_lines.append(f"PROPS: {self.props}")
        print_lines.append("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return "\n".join(print_lines)
    
#--------------------------LEAF NODE DECLARATION--------------------------    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value: 
            raise ValueError("ERROR: Leafnode has no value")
        
        if not self.tag:
            return self.value
        
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        print_lines = []
        print_lines.append("xxxxxxxxxxxxxxxxxxHTML NODExxxxxxxxxxxxxxxxxxxxxxxx")
        print_lines.append(f"TAG: {self.tag}")
        print_lines.append(f"VALUE: {self.value}")
        print_lines.append(f"PROPS: {self.props}")
        print_lines.append("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return "\n".join(print_lines)
    
#-------------------------PARENT NODE DECLARATION-------------------------
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("ERROR: Parentnode has no tag")
        
        if not self.children:
            raise ValueError("ERROR: Parentnode has no children")
        
        output = f"<{self.tag}>"

        for child in self.children:
            output += f"{child.to_html()}"

        output += f"</{self.tag}>"

        return output