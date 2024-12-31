from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        if value is None:
            raise ValueError
        super().__init__(
                tag = tag,
                value = value,
                props = props
                )
    def to_html(self):
        if self.tag is None:
            return f'{self.value}'
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
