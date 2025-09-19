import unittest

from py_static_gen.textnode import TextNode, TextType

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

    
if __name__ == "__main__":
    unittest.main()