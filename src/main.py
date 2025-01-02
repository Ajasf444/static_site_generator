from textnode import TextNode
from leafnode import LeafNode

def main():
    text_node = TextNode('This is a text node', TextType.BOLD, 'https://www.boot.dev')
    print(text_node)

def text_node_to_leaf_node(text_node):
    pass

if __name__ == '__main__':
    main()
