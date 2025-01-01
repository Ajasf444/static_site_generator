from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if children is None:
            raise ValueError("ParentNode must have children")
        if len(children) == 0:
            raise ValueError("Parentnode must have at least one child")
        super().__init__(tag, None, children, props)

    def to_html(self):
        children_html = ''
        for child in self.children:
            children_html += child.to_html()
        return f'<{self.tag}>{children_html}</{self.tag}>'

