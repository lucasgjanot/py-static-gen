from py_static_gen.htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        
        if not self.children:
            raise ValueError("ParentNode must have children")

        child_html = ""
        for node in self.children:
            child_html += node.to_html()

        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
        