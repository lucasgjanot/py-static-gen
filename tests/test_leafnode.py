import unittest
from py_static_gen.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        cases = [
        ("p", "This is a paragraph of text.", None, "<p>This is a paragraph of text.</p>"),
        ("a", "Click me!", {"href": "https://www.google.com"}, '<a href="https://www.google.com">Click me!</a>'),
        ]
        for tag, value, props,expected in cases:
            with self.subTest(tag=tag, value=value,props=props):
                leaf = LeafNode(tag, value, props)
                self.assertEqual(leaf.to_html(), expected)
    
    def test_to_html_no_value(self):
        leaf=LeafNode("p", None)
        with self.assertRaises(ValueError):
            leaf.to_html()
        
    def test_to_html_no_tag(self):
        leaf=LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "This is a paragraph of text.")

if __name__ == "__main__":
    unittest.main()