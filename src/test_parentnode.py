import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_no_tag_raises_error(self):
        self.assertRaises(ValueError, lambda: ParentNode(None, None))
    def test_no_children_raises_error(self):
        self.assertRaises(ValueError, lambda: ParentNode('a', None))
    def test_empty_children_raises_error(self):
        self.assertRaises(ValueError, lambda: ParentNode('a', []))
    def test_multiple_leaf_children(self):
        parent_node = ParentNode(
                'p',
                [
                    LeafNode('b', 'Bold text'),
                    LeafNode(None, 'Normal text'),
                    LeafNode('i', 'Italic text'),
                    LeafNode(None, 'Normal text'),
                    ],
                )
        expected ='<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>' 
        self.assertEqual(parent_node.to_html(), expected)
    def test_single_leaf_child(self):
        parent_node = ParentNode(
                'p',
                [
                    LeafNode('b', 'Bold text'),
                    ],
                )
        expected = '<p><b>Bold text</b></p>'
        self.assertEqual(parent_node.to_html(), expected)
    
    def test_single_parent_node_as_child(self):
        parent_node = ParentNode(
                'p',
                [
                    ParentNode('i', [
                        LeafNode('b', 'Bold text'),
                        ]
                               )
                    ]
                )
        expected = '<p><i><b>Bold text</b></i></p>'
        self.assertEqual(parent_node.to_html(), expected)

if __name__ == '__main__':
    unittest.main()
