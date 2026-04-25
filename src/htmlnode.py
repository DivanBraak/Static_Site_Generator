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
        #output_list = []
        output = ""
        for prop in self.props:
            output += f' {prop}="{self.props[prop]}"'
            #output_list.append(f"{prop}={self.props[prop]}")
        return output #" ".join(output_list)
    
    def __repr__(self):
        print_lines = []
        print_lines.append("xxxxxxxxxxxxxxxxxxHTML NODExxxxxxxxxxxxxxxxxxxxxxxx")
        print_lines.append(f"TAG: {self.tag}")
        print_lines.append(f"VALUE: {self.value}")
        print_lines.append(f"CHILDREN: {self.children}")
        print_lines.append(f"PROPS: {self.props}")
        print_lines.append("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        return "\n".join(print_lines)
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
    
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