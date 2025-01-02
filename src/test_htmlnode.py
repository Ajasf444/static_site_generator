import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_get_tag(self):
        node = HTMLNode(tag = 'baconator fries')
        self.assertEqual(node.tag, 'baconator fries')
    def test_get_value(self):
        node = HTMLNode(value = 'baconator fries')
        self.assertEqual(node.value, 'baconator fries')
    def test_get_children(self):
        node = HTMLNode(children = ['baconator', 'fries'])
        self.assertEqual(node.children, ['baconator', 'fries'])
    def test_props_to_html(self):
        node = HTMLNode(props = {'baconator': 'fries', 'Tahm': 'Kench'})
        self.assertEqual(node.props_to_html(), ' baconator="fries" Tahm="Kench"')
    def test_emtpy_props_to_html(self):
        node = HTMLNode(props = {})
        self.assertEqual(node.props_to_html(), '')


if __name__ == '__main__':
    unittest.main()
