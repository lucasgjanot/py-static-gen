import unittest
from enum import Enum
from py_static_gen.textnode import TextNode, TextType
from py_static_gen.nodeconverter import text_node_to_html_node


class FakeTextType(Enum):
    UNKNOWN = "unknown"

class TestNodeConverter(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, node.text)

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, node.text)

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, node.text)

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK , url="https://exemple.com" )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, node.text)
        self.assertEqual(html_node.props, {"href": "https://exemple.com"})

    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE , url="https://exemple.com" )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://exemple.com", "alt": node.text})

    def test_invalid_text_type_raises(self):
        invalid_node = TextNode("Some text", FakeTextType.UNKNOWN)

        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(invalid_node)

        self.assertIn("invalid text type", str(cm.exception))
