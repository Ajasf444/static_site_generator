from textnode import TextNode
from leafnode import LeafNode

def main():
    text_node = TextNode('This is a text node', TextType.BOLD, 'https://www.boot.dev')
    print(text_node)

def text_node_to_html_node(text_node):
    text_type = text_node.text_type
    text = text_node.text
    url = text_node.url

    match text_type:
        case NORMAL:
            return LeafNode(None, text)
        case BOLD:
            return LeafNode('b', text)
        case ITALIC:
            return LeafNode('i', text)
        case CODE:
            return LeafNode('code', text)
        case LINK:
            return LeafNode('a', text)
        case IMAGE:
            return LeafNode('img', None, {'src': url, 'alt': text})
        case _:
            raise ValueError("Invalid TextType")

if __name__ == '__main__':
    main()
