import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_missing_value_should_error(self):
        self.assertRaises(ValueError, lambda: LeafNode(None, None, None))
    
    def test_get_tag(self):
        leaf_node = LeafNode('tag', 'value', {})
        self.assertEqual(leaf_node.tag, 'tag')

    def test_get_value(self):
        leaf_node = LeafNode('tag', 'value', {})
        self.assertEqual(leaf_node.value, 'value')

    def test_props_to_html_without_tag(self):
        leaf_node = LeafNode(None, 'Baconator Fries', {'Tahm': 'Kench'})
        self.assertEqual(leaf_node.to_html(), 'Baconator Fries')
    
    def test_props_to_html_with_tag(self):
        leaf_node = LeafNode('a', 'Baconator Fries', {'Tahm': 'Kench'})
        correct_html = '<a Tahm="Kench">Baconator Fries</a>'
        self.assertEqual(leaf_node.to_html(), correct_html)
        


if __name__ == '__main__':
    unittest.main()
