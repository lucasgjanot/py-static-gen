import unittest
from py_static_gen.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr_format(self):
        node = HTMLNode("h1","Teste")
        self.assertEqual(repr(node), "HTMLNode(h1, Teste, children: None, None)")
        
if __name__ == "__main__":
    unittest.main()