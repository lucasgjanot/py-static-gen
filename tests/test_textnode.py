import unittest
from enum import Enum
from py_static_gen.textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):

    def test_equal_nodes(self):
        node1 = TextNode("Texto Teste", TextType.BOLD)
        node2 = TextNode("Texto Teste", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_different_text_type(self):
        node1 = TextNode("Texto Teste", TextType.TEXT)
        node2 = TextNode("Texto Teste", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_different_text_content(self):
        node1 = TextNode("Um texto", TextType.TEXT)
        node2 = TextNode("Outro texto", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_nodes_with_url(self):
        node1 = TextNode("Google", TextType.LINK, "https://google.com")
        node2 = TextNode("Google", TextType.LINK, "https://google.com")
        self.assertEqual(node1, node2)

    def test_different_url(self):
        node1 = TextNode("Google", TextType.LINK, "https://google.com")
        node2 = TextNode("Google", TextType.LINK, "https://bing.com")
        self.assertNotEqual(node1, node2)

    def test_repr_format(self):
        node = TextNode("Exemplo", TextType.ITALIC, None)
        self.assertEqual(repr(node), "TextNode(Exemplo, italic, None)")


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

if __name__ == "__main__":
    unittest.main()